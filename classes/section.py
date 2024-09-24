# %% Definitions

''' Main assumptions:
- First point is the trailing edge
- Direction of the splines are bot curve and then top curve
- Same number of points for bot and top curve when imported from Station
- Number of points is 50 or bigger (Need to get rid of this one eventually)'''

# Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from shapely import LineString, offset_curve, Polygon

from utils.utils import (splineConstructor, lineConstructor, skinOverlapLocator,
                         splineIntersection, trailingEdgeThickness)
from classes.station import Station


# functions
def figProperties(ax, title:str, xlabel:str ='x [-]',
                  ylabel:str ='y [-]', labelsize:str ='large',
                  legend:bool = True) -> None:
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.minorticks_on()
    ax.tick_params(axis='both', which='both', direction='in', top=True,
                   right=True, labelsize=labelsize)
    ax.grid(which='major')
    ax.axis('equal')
    if legend:
        ax.legend()
    ax.set_title(title)
    plt.tight_layout()

# Main Class
class Section:
    def __init__(self,
                 station:Station,
                 n_plies:int,
                 ply_thickness:float,
                 overlap_target:float,
                 te_thickness:float = 8,
                 saveFig:bool = False,
                 tolerance:int = 6, # Tolerance for decimal places ACIS
                ) -> None:
        
        # Parameters
        self.parameters = {'n_plies': n_plies,
                           'ply_thickness': ply_thickness,
                           'overlap_target': overlap_target,
                           'te_thickness': te_thickness,
                           'saveFig': saveFig,
                           'base_airfoil': station.airfoil,
                           'z':station.parameters['offset'][2]
                           }
        
        # self.splines = {} defined later
        self.guides = {}
        self.indexes = {}
        self.indexes['idx_ply_cut_bot'] = {}
        self.indexes['idx_ply_cut_top'] = {}
        
        self.t = {x:{} for x in ['t_bot','t_splines_bot','t_plies_bot',
                                 't_top','t_splines_top','t_plies_top']}
        
        self.figs = {}
        self.figs['bottom_ply'] = {}
        self.figs['top_ply'] = {}
        
        self.name = 'skin_' + str(station.parameters['offset'][2])
        
        # Offset curves
        # curve_0 = LineString(station.xy)
        # curves_offset = {0:station.xy}
        # for i in range(ply_thickness,ply_thickness*(n_plies+1)):
        #     curves_offset[i] = np.array(offset_curve(curve_0,-i).coords)
            
        ###---- Alternative -------
        curve_0 = Polygon(station.xy)
        curves_offset = {0:station.xy}
        # for i in range(ply_thickness,ply_thickness*(n_plies+1)):
        for i in range(1,n_plies+1):
            thk = round(ply_thickness*i,2)
            curves_offset[i] = np.array(curve_0.buffer(-thk).exterior.coords)
            
        # Chord line
        chord_line = lineConstructor(p0 = station.xy[0],
                        p1 = station.xy[int(np.floor(len(station.xy)/2))])
        self.guides['line_chord'] = chord_line
        
        # Splines
        splines = {x:splineConstructor(curves_offset[x]) for
                   x in range(n_plies+1)}
        self.splines = splines
        
        # Index LE
        idx_LE = {x:round(splineIntersection(splines[x],chord_line,21),tolerance)
                  for x in range(n_plies+1)}
        self.indexes['idx_LE'] = idx_LE
        
        # Full skin graph
        fig, ax = plt.subplots(figsize=(10,6))

        for i in range(n_plies+1):
            
            t = np.arange(0,len(splines[i]['x'].x))
            
            ax.plot(splines[i]['x'](t),splines[i]['y'](t), 
                    label = f'Curve {i}', linewidth = 0.15)
            
            ax.scatter(splines[i]['x'](idx_LE[i]),splines[i]['y'](idx_LE[i]), 
                        label = None, marker='x',s=0.5)
            
        ### Figure properties
        figProperties(ax=ax, title=f'Full Skin - {n_plies} plies')
        
        self.figs['section'] = fig
        if saveFig:
            fig.savefig('skin.png',dpi=800)
        plt.close(fig)
        
        if station.parameters['isCircle']:
            idx_olp_sta = {x:idx_LE[x] for x in range(n_plies+1)}
            overlap_line = chord_line
            self.indexes['idx_olp_sta'] = idx_olp_sta
            
        else:
            # Locate overlap
            p_ref = np.array([splines[0]['x'](idx_LE[0]),
                            splines[0]['y'](idx_LE[0])])
            
            t_target = skinOverlapLocator(overlap_target,p_ref,
                        station.parameters['twist_angle'], splines[0],idx_LE[0])

            p0 = np.array([splines[0]['x'](t_target,0),
                        splines[0]['y'](t_target,0)])
            p1 = p0 + np.array([-splines[0]['y'](t_target,1),
                                splines[0]['x'](t_target,1)])

            overlap_line = lineConstructor(p0 = tuple(p0), p1 = tuple(p1))
            idx_olp_sta = {0:t_target}

            ### Cut all other lines at this point
            for i in range(1,n_plies+1):
                idx_olp_sta[i] = splineIntersection(splines[i],overlap_line,idx_LE[i])
                
            ### Store variables
            self.guides['line_overlap_start'] = overlap_line
            self.indexes['idx_olp_sta'] = idx_olp_sta
        
        # Bottom skin plot
        fig, ax = plt.subplots(figsize=(10,6))
        
        for i in range(n_plies+1):
            
            t = np.arange(int(np.ceil(idx_olp_sta[i]))).tolist()
            
            if idx_olp_sta[i] % int(idx_olp_sta[i]) != 0:
                t += [idx_olp_sta[i]]
                
            self.t['t_bot'][i] = t
            
            ax.plot(splines[i]['x'](t),splines[i]['y'](t), 
                    label = f'Curve {i}', linewidth = 0.2)
            
        y_line = np.arange(ax.get_ylim()[0],ax.get_ylim()[1])
        x_line = (y_line - overlap_line['b']) / overlap_line['m']
        
        ax.plot(x_line, y_line, label='Skin Overlap', lw=0.2)
        
        ### Figure properties
        figProperties(ax=ax, title='Bottom Skin')
        
        self.figs['bottom'] = fig
        if saveFig:
            fig.savefig('bottom_skin.png',dpi=800)
        plt.close(fig)
        
        if station.parameters['isCircle']:
            idx_te_bot = {x:0 for x in range(n_plies+1)}
            te_line = lineConstructor(p0 = (splines[0]['x'](0),
                                            splines[0]['y'](0)),
                                      ang = chord_line['nor'])
        
        else:
            # Cut trailing edge
            idx_TE_bot, idx_TE_top = trailingEdgeThickness(te_thickness,
                                                        splines[0])
            
            te_line = lineConstructor(p0 = (splines[0]['x'](idx_TE_bot),
                                            splines[0]['y'](idx_TE_bot)),
                                    p1 = (splines[0]['x'](idx_TE_top),
                                            splines[0]['y'](idx_TE_top)))
            
            idx_te_bot = {x:splineIntersection(splines[x],te_line) 
                        for x in range(n_plies+1)}
        
        ### Store variables
        self.guides['line_te'] = te_line
        
        # Bottom graph with te trimmed
        fig, ax = plt.subplots(figsize=(10,6))

        for i in range(n_plies+1):
            
            if idx_te_bot[i] == None or idx_te_bot[i] == 0:
                idx_te_bot[i] = 0
                t = []
            else:
                t = [idx_te_bot[i]]
            
            t += np.arange(np.ceil(idx_te_bot[i]),np.ceil(idx_olp_sta[i])).tolist()
            
            if idx_olp_sta[i] % int(idx_olp_sta[i]) == 0:
                t += [idx_olp_sta[i]]
            
            self.t['t_splines_bot'][i] = t
            
            x_curve = splines[i]['x'](t)
            y_curve = splines[i]['y'](t)
            
            ax.plot(x_curve,
                    y_curve, 
                    label = f'Curve {i}',
                    linewidth = 0.2)

        x_lims = ax.get_xlim()
        y_lims = ax.get_ylim()

        # Overlap line plot
        y_line = np.arange(y_lims[0],y_lims[1])
        x_line = (y_line - overlap_line['b']) / overlap_line['m']
        ax.plot(x_line,y_line,'r--',label='Skin Overlap', lw=0.3)

        # TE line plot
        y_line = np.arange(y_lims[0],y_lims[1])
        x_line = (y_line - te_line['b']) / te_line['m']
        ax.plot(x_line,y_line,'r--',label='TE cut', lw=0.3)

        # Figure properties
        figProperties(ax=ax, title='Bottom Skin after leading edge trim')
        ax.set_xlim(x_lims)
        ax.set_ylim(y_lims)

        self.figs['bottom_trim'] = fig
        if saveFig:
            fig.savefig('bottom_skin_2.png',dpi=800)
        plt.close(fig)
            
        ### Store variables
        self.indexes['idx_te_bot'] = idx_te_bot
        
        # Individual TE trim for plies
        if station.parameters['isCircle']:
            self.indexes['idx_ply_cut_bot'] = {}
            
        else:
            for i in range(n_plies-1,-1,-1):
                
                dx = splines[i]['x'](idx_te_bot[i]) - splines[i+1]['x'](idx_te_bot[i+1])
                dy = splines[i]['y'](idx_te_bot[i]) - splines[i+1]['y'](idx_te_bot[i+1])
                beta = np.arctan2(dy,dx)
                alpha = te_line['tan']

                d = np.sqrt(dx**2 + dy**2) * np.sin(beta - alpha)

                if np.abs(d) > 1: # [mm]
                    # print(f'Curve {i} does need trim.')
                    
                    line_cut = lineConstructor(p0=(splines[i+1]['x'](idx_te_bot[i+1]),
                                                splines[i+1]['y'](idx_te_bot[i+1])),
                                            ang=te_line['tan'])
                    self.indexes['idx_ply_cut_bot'][i] = splineIntersection(
                        splines[i], line_cut, idx_te_bot[i])
                
        # Ply curves
        t_plies_bot = {}
        for i in range(n_plies):
            t_plies_bot[i+1] = {}
            
            if i not in self.indexes['idx_ply_cut_bot'].keys():
                t_plies_bot[i+1][i] = self.t['t_splines_bot'][i]
            else:
                t_plies_bot[i+1][i] = [self.indexes['idx_ply_cut_bot'][i]] + \
                    [x for x in self.t['t_splines_bot'][i] if
                     x > self.indexes['idx_ply_cut_bot'][i]]
                
            t_plies_bot[i+1][i+1] = self.t['t_splines_bot'][i+1]
        
        ### Store variables
        self.t['t_plies_bot'] = t_plies_bot
            
        # Generate ply graphs
        for i in range(1,n_plies+1):
            
            fig, ax = plt.subplots(figsize=(10,6))
            
            idx_curves = list(t_plies_bot[i].keys())
            
            c1 = splines[idx_curves[0]]
            c2 = splines[idx_curves[1]]
            
            ax.plot(c1['x'](t_plies_bot[i][idx_curves[0]]),
                    c1['y'](t_plies_bot[i][idx_curves[0]]),
                    label = 'Outer curve')
            
            ax.plot(c2['x'](t_plies_bot[i][idx_curves[1]]),
                    c2['y'](t_plies_bot[i][idx_curves[1]]),
                    label = 'Inner curve')
            
            # TE side line
            x_edge_right = (c1['x'](t_plies_bot[i][idx_curves[0]][0]),
                            c2['x'](t_plies_bot[i][idx_curves[1]][0]))
            y_edge_right = (c1['y'](t_plies_bot[i][idx_curves[0]][0]),
                            c2['y'](t_plies_bot[i][idx_curves[1]][0]))
            
            ax.plot(x_edge_right, y_edge_right, label = 'Right edge')
            
            # Left edge line
            x_edge_right = (c1['x'](t_plies_bot[i][idx_curves[0]][-1]),
                            c2['x'](t_plies_bot[i][idx_curves[1]][-1]))
            y_edge_right = (c1['y'](t_plies_bot[i][idx_curves[0]][-1]),
                            c2['y'](t_plies_bot[i][idx_curves[1]][-1]))
            
            ax.plot(x_edge_right, y_edge_right, label = 'Left edge')
            
            # Figure properties
            figProperties(ax=ax, title=f'Bottom - Ply {i}')
            
            self.figs['bottom_ply'][i] = fig    
            if saveFig:
                fig.savefig(f'Ply{i}_bot.png', dpi=800)
            plt.close(fig)
                
        # Top skin graph
        fig, ax = plt.subplots(figsize=(10,6))

        for i in range(n_plies+1):
            
            if idx_olp_sta[i] % int(idx_olp_sta[i]) != 0:
                t = [idx_olp_sta[i]]
            else:
                t = []
                
            t += np.arange(np.ceil(idx_olp_sta[i]), splines[i]['u'] + 1).tolist()
            
            self.t['t_top'][i] = t
            
            ax.plot(splines[i]['x'](t), splines[i]['y'](t), label=f'Curve {i}')
            
            ### Figure properties
            figProperties(ax=ax, title='Before trailing edge cut')
            
            self.figs['top'] = fig
            if saveFig:
                fig.savefig('top.png', dpi=800)
            plt.close(fig)
                
        # Trailing edge cut
        if station.parameters['isCircle']:
            idx_te_top = {x:None for x in range(n_plies+1)}
        
        else:
            idx_te_top = {x:splineIntersection(splines[x],te_line,idx_olp_sta[i]) 
                for x in range(n_plies+1)}
        
        fig, ax = plt.subplots(figsize=(10,6))

        for i in range(n_plies+1):
            
            if idx_olp_sta[i] % int(idx_olp_sta[i]) != 0:
                t = [idx_olp_sta[i]]
            else:
                t = []
            
            if idx_te_top[i] == None:
                t += np.arange(np.ceil(idx_olp_sta[i]), splines[i]['u']+1).tolist()
            else:
                t += np.arange(np.ceil(idx_olp_sta[i]), np.ceil(idx_te_top[i])).tolist()
                
                if idx_te_top[i] % int(idx_te_top[i]) == 0:
                    t += [idx_te_top[i]]
            
            self.t['t_splines_top'][i] = t
            
            ax.plot(splines[i]['x'](t), splines[i]['y'](t), label=f'Curve {i}')
            
            # Figure properties
            figProperties(ax=ax, title='After trailing edge cut')
            
            self.figs['top_trim'] = fig
            if saveFig:
                fig.savefig('top_trim.png',dpi=800)
            plt.close(fig)
                
        # Spline trim for plies
        if not station.parameters['isCircle']:
            
            for i in range(n_plies):
        
                if idx_te_top[i] is None:
                    idx_te_top[i] = splines[i]['u']
                    
                if idx_te_top[i+1] is None:
                    idx_te_top[i+1] = splines[i+1]['u']

                dx = splines[i]['x'](idx_te_top[i]) - splines[i+1]['x'](idx_te_top[i+1])
                dy = splines[i]['y'](idx_te_top[i]) - splines[i+1]['y'](idx_te_top[i+1])
                beta = np.arctan2(dy,dx)
                alpha = te_line['tan']

                d = np.sqrt(dx**2 + dy**2) * np.sin(beta - alpha)

                if np.abs(d) > 1: # [mm]
                    print(f'Curve {i} does need trim.')
                    
                    line_cut = lineConstructor(p0=(splines[i+1]['x'](idx_te_top[i+1]),
                                                splines[i+1]['y'](idx_te_top[i+1])),
                                            ang=te_line['tan'])
                    self.indexes['idx_ply_cut_top'][i] = splineIntersection(
                        splines[i], line_cut, idx_olp_sta[i])
        
        ### Store variables
        self.indexes['idx_te_top'] = idx_te_top
        
        # Store t for each ply
        t_plies_top = {}
        for i in range(n_plies):
            t_plies_top[i+1] = {}
            
            if i not in self.indexes['idx_ply_cut_top'].keys():
                t_plies_top[i+1][i] = self.t['t_splines_top'][i]
            else:
                t_plies_top[i+1][i] = [x for x in self.t['t_splines_top'][i] if 
                    x < self.indexes['idx_ply_cut_top'][i]] + \
                        [self.indexes['idx_ply_cut_top'][i]]
                
            t_plies_top[i+1][i+1] = self.t['t_splines_top'][i+1]
            
        ### Store variables
        self.t['t_plies_top'] = t_plies_top
        
        # Generate top plies
        for i in range(1,n_plies+1):
            
            fig, ax = plt.subplots(figsize=(10,6))
            
            idx_curves = list(t_plies_top[i].keys())
            
            c1 = splines[idx_curves[0]]
            c2 = splines[idx_curves[1]]
            
            ax.plot(c1['x'](t_plies_top[i][idx_curves[0]]),
                    c1['y'](t_plies_top[i][idx_curves[0]]),
                    label = 'Outer curve')
            
            ax.plot(c2['x'](t_plies_top[i][idx_curves[1]]),
                    c2['y'](t_plies_top[i][idx_curves[1]]),
                    label = 'Inner curve')
            
            # TE side line
            x_edge_right = (c1['x'](t_plies_top[i][idx_curves[0]][0]),
                            c2['x'](t_plies_top[i][idx_curves[1]][0]))
            y_edge_right = (c1['y'](t_plies_top[i][idx_curves[0]][0]),
                            c2['y'](t_plies_top[i][idx_curves[1]][0]))
            
            ax.plot(x_edge_right, y_edge_right, label = 'Right edge')
            
            # Left edge line
            x_edge_right = (c1['x'](t_plies_top[i][idx_curves[0]][-1]),
                            c2['x'](t_plies_top[i][idx_curves[1]][-1]))
            y_edge_right = (c1['y'](t_plies_top[i][idx_curves[0]][-1]),
                            c2['y'](t_plies_top[i][idx_curves[1]][-1]))
            
            ax.plot(x_edge_right, y_edge_right, label = 'Left edge')
            
            # Figure properties
            figProperties(ax=ax, title=f'Top - Ply {i}')
            
            self.figs['top_ply'][i] = fig
            if saveFig:
                fig.savefig(f'Ply{i}_top.png', dpi=800)
            plt.close(fig)
        

# %% Example

if __name__ == '__main__':
    
    # Arguments
    sta = Station(chord=1334,
                  twist_angle=24.3,
                  x_offset=-474.26,
                  y_offset=255,
                  z_offset=1500,
                  y_multiplier=1.55,
                  y_mirror=True,
                #   path=os.path.join(os.getcwd(),'airfoils','NACA63430.txt'),
                  path=os.path.join(os.getcwd(),'airfoils','circle.txt'),
                  )
    offset_distance = 1
    n_plies = 8
    saveFig = False
    overlap_target = 200
    trailing_edge_thickness = 8 # mm
    
    db = Section(station=sta, n_plies=n_plies, ply_thickness=offset_distance,
                 overlap_target=overlap_target,
                 te_thickness=trailing_edge_thickness, saveFig=saveFig)
    
    db.figs['top_ply'][1]
