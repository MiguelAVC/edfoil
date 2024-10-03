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
                           'z':station.parameters['offset'][2],
                           'twist_angle': station.parameters['twist_angle']
                           }
        
        # self.splines = {} defined later
        self.lines = {}
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
        for i in range(1,n_plies+1):
            thk = round(ply_thickness*i,2)
            c_buffer = curve_0.buffer(-thk)
            c_simplified = c_buffer.simplify(tolerance=0.01)
            curves_offset[i] = np.array(c_simplified.exterior.coords)
            
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
        
        # Split in overlap
        if station.parameters['isCircle']:
            idx_olp_sta = {x:{0:idx_LE[x]} for x in range(n_plies+1)}
            idx_top_sta = {x:idx_LE[x] for x in range(n_plies+1)}
            overlap_line = chord_line
            self.indexes['idx_olp_sta'] = idx_olp_sta
            self.indexes['idx_top_sta'] = idx_top_sta
            
        else:
            # Locate overlap
            
            # Reference point at the leading edge
            p_ref = np.array([splines[0]['x'](idx_LE[0]),
                            splines[0]['y'](idx_LE[0])])
            
            t_target = skinOverlapLocator(d_target=overlap_target, p0= p_ref,
                        twist_ang=station.parameters['twist_angle'], spline=splines[0], u0=idx_LE[0])
            
            # Intersection coordinates
            p0 = np.array([splines[0]['x'](t_target,0),
                        splines[0]['y'](t_target,0)])
            p1 = p0 + np.array([-splines[0]['y'](t_target,1),
                                splines[0]['x'](t_target,1)])
            
            overlap_line = lineConstructor(p0 = tuple(p0), p1 = tuple(p1))
            
            # Offset overlap line
            self.guides['line_overlap_offset'] = {}
            idx_olp_sta = {}
            idx_top_sta = {i:splineIntersection(spline=splines[i], line= overlap_line, u0=idx_LE[i]) for i in range(n_plies+1)}
            # idx_olp_sta = {0:t_target}

            ### Cut all other lines at this point
            for i in range(n_plies+1):
            # for i in range(1,n_plies+1):
                idx_olp_sta[i] = {}
                
                x0 = ply_thickness * (i+1) * np.cos(overlap_line['nor']) + overlap_line['p'][0]
                y0 = ply_thickness * (i+1) * np.sin(overlap_line['nor']) + overlap_line['p'][1]
                p0 = tuple([x0, y0])
                
                offset_olp_line = lineConstructor(p0 = p0, ang = overlap_line['tan'])
                self.guides['line_overlap_offset'][i] = offset_olp_line
                
                idx_olp_sta[i][0] = splineIntersection(spline=splines[i], line=offset_olp_line, u0=idx_LE[i])
                
                if i < n_plies:
                    idx_olp_sta[i][1] = splineIntersection(spline=splines[i+1], line=offset_olp_line, u0=idx_LE[i])
                
            ### Store variables
            self.guides['line_overlap_start'] = overlap_line
            self.indexes['idx_olp_sta'] = idx_olp_sta
            self.indexes['idx_top_sta'] = idx_top_sta
        
        # Bottom skin plot
        fig, ax = plt.subplots(figsize=(10,6))
        
        for i in range(n_plies+1):
            
            t = np.arange(int(np.ceil(idx_olp_sta[i][0]))).tolist()
            
            if idx_olp_sta[i][0] % int(idx_olp_sta[i][0]) != 0:
                t += [idx_olp_sta[i][0]]
                
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
            
            t += np.arange(np.ceil(idx_te_bot[i]),np.ceil(idx_olp_sta[i][0])).tolist()
            t += [idx_olp_sta[i][0]]
            
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

                if np.abs(d) > 0.5 * ply_thickness: # [mm]
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
                
            if station.parameters['isCircle']:
            
                t_plies_bot[i+1][i+1] = self.t['t_splines_bot'][i+1]
                
            else:
            
                if idx_te_bot[i+1] == 0:
                    t = []
                else:
                    t = [idx_te_bot[i+1]]
                
                t += np.arange(np.ceil(idx_te_bot[i+1]),np.ceil(idx_olp_sta[i][1])).tolist()
                t += [idx_olp_sta[i][1]]
                
                t_plies_bot[i+1][i+1] = t
        
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
            
            if idx_top_sta[i] % int(idx_top_sta[i]) != 0:
                t = [idx_top_sta[i]]
            else:
                t = []
                
            t += np.arange(np.ceil(idx_top_sta[i]), splines[i]['u'] + 1).tolist()
            
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
            idx_te_top = {x:splineIntersection(splines[x],te_line,idx_top_sta[i]) 
                for x in range(n_plies+1)}
        
        fig, ax = plt.subplots(figsize=(10,6))

        for i in range(n_plies+1):
            
            if idx_top_sta[i] % int(idx_top_sta[i]) != 0:
                t = [idx_top_sta[i]]
            else:
                t = []
            
            if idx_te_top[i] == None:
                t += np.arange(np.ceil(idx_top_sta[i]), splines[i]['u']+1).tolist()
            else:
                t += np.arange(np.ceil(idx_top_sta[i]), np.ceil(idx_te_top[i])).tolist()
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

                if np.abs(d) > 0.5 * ply_thickness: # [mm]
                    print(f'Curve {i} does need trim.')
                    
                    line_cut = lineConstructor(p0=(splines[i+1]['x'](idx_te_top[i+1]),
                                                splines[i+1]['y'](idx_te_top[i+1])),
                                            ang=te_line['tan'])
                    self.indexes['idx_ply_cut_top'][i] = splineIntersection(
                        splines[i], line_cut, idx_top_sta[i])
        
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
        
    def plotSection(self):
        
        fig, ax = plt.subplots(figsize=(10,6))
        
        n_plies = self.parameters['n_plies']
        t_plies = [self.t['t_plies_top'], self.t['t_plies_bot']]
        
        cmap = plt.get_cmap('rainbow')
        colours = [cmap(x/n_plies) for x in range(n_plies)]
        
        for i in range(1,n_plies+1):
            
            for j in range(2):
                
                label = f'Ply {i}' if j == 0 else None
                    
                idx_c = list(t_plies[j][i].keys())
            
                c1 = self.splines[idx_c[0]]
                c2 = self.splines[idx_c[1]]
                
                ax.plot(c1['x'](t_plies[j][i][idx_c[0]]),
                        c1['y'](t_plies[j][i][idx_c[0]]),
                        label = label, c = colours[i-1])
                
                ax.plot(c2['x'](t_plies[j][i][idx_c[1]]),
                        c2['y'](t_plies[j][i][idx_c[1]]),
                        label = None, c = colours[i-1])
                
                # TE side line
                x_edge_right = (c1['x'](t_plies[j][i][idx_c[0]][0]),
                                c2['x'](t_plies[j][i][idx_c[1]][0]))
                y_edge_right = (c1['y'](t_plies[j][i][idx_c[0]][0]),
                                c2['y'](t_plies[j][i][idx_c[1]][0]))
                
                ax.plot(x_edge_right, y_edge_right, label = None, c = colours[i-1])
                
                # Left edge line
                x_edge_right = (c1['x'](t_plies[j][i][idx_c[0]][-1]),
                                c2['x'](t_plies[j][i][idx_c[1]][-1]))
                y_edge_right = (c1['y'](t_plies[j][i][idx_c[0]][-1]),
                                c2['y'](t_plies[j][i][idx_c[1]][-1]))
                
                ax.plot(x_edge_right, y_edge_right, label = None, c = colours[i-1])
            
            # Figure properties
            figProperties(ax=ax, title=f'Full Section')
            
            self.figs['full'] = fig
            if saveFig:
                fig.savefig(f'Section.png', dpi=800)
            plt.close(fig)
            
    def jiggle(self, overlap_dist:float):
        
        n_plies = self.parameters['n_plies']
        last_spline = self.splines[n_plies]
        
        lspl_t = np.arange(np.floor(self.indexes['idx_LE'][n_plies]), last_spline['u']+1)
        lspl_x = last_spline['x'](lspl_t)
        lspl_y = last_spline['y'](lspl_t)
        lspl_xy = list(zip(lspl_x,lspl_y))
        
        curve_0 = Polygon(lspl_xy)
        c_offset = {}
        for i in range(n_plies+1):
            thk = round(self.parameters['ply_thickness']*i +1,2)
            c_buffer = curve_0.buffer(-thk)
            c_simplified = c_buffer.simplify(tolerance=0.01)
            c_offset[i] = splineConstructor(np.array(c_simplified.exterior.coords))
        
        # Overlap end guide
        p_olp_sta = self.guides['line_overlap_start']['p']
        t_target = skinOverlapLocator(d_target=overlap_dist, p0=p_olp_sta,
            twist_ang=self.parameters['twist_angle'], spline=c_offset[0], u0=0)
        
        # Intersection coordinates
        p0 = np.array([c_offset[0]['x'](t_target,0),
                    c_offset[0]['y'](t_target,0)])
        p1 = p0 + np.array([-c_offset[0]['y'](t_target,1),
                            c_offset[0]['x'](t_target,1)])
        
        line_olp_end = lineConstructor(p0 = tuple(p0), p1 = tuple(p1))
        
        # Finding t-parameter (per ply)
        t_target = {}
        
        for i in range(1,n_plies+1):
            t_target[i] = {}
            
            line_start = self.guides['line_overlap_offset'][i]
            line_end = line_olp_end
            
            # First curve of ply
            t_target[i][i-1] = {}
            t_target[i][i-1][0] = splineIntersection(spline=c_offset[i-1], line=line_start, u0=0)
            t_target[i][i-1][1] = splineIntersection(spline=c_offset[i-1], line=line_end, u0=t_target[i][i-1][0])
            
            # Second curve of ply
            t_target[i][i] = {}
            t_target[i][i][0] = splineIntersection(spline=c_offset[i], line=line_start, u0=0)
            t_target[i][i][1] = splineIntersection(spline=c_offset[i], line=line_end, u0=t_target[i][i][0])
            
        # Create t-parameter list for each ply
        t_bot_3 = {}
        
        for i in range(1,n_plies+1):
            t_bot_3[i] = {}
            
            for j in list(t_target[i].keys()):
                
                if t_target[i][j][0] % int(t_target[i][j][0]) == 0:
                    t_bot_3[i][j] = []
                else:
                    t_bot_3[i][j] = [float(t_target[i][j][0])]
                
                t_bot_3[i][j] += np.arange(np.ceil(t_target[i][j][0]),np.ceil(t_target[i][j][1])).tolist()
                t_bot_3[i][j] += [float(t_target[i][j][1])]
        
        self.t['t_bot_3'] = t_bot_3
        
        # Jiggle PART 2 (Vertical part)
        x_bot_2 = {}
        y_bot_2 = {}
        for i in range(1,n_plies+1):
            x_bot_2[i] = []
            y_bot_2[i] = []
            # Point 1
            if i < n_plies:
                x_bot_2[i].append(self.splines[i]['x'](self.t['t_plies_bot'][i+1][i][-1]))
                y_bot_2[i].append(self.splines[i]['y'](self.t['t_plies_bot'][i+1][i][-1]))
            else:
                t_target = splineIntersection(spline=self.splines[i], 
                    line=self.guides['line_overlap_offset'][i], u0=self.indexes['idx_LE'][i])
                
                x_bot_2[i].append(self.splines[i]['x'](t_target))
                y_bot_2[i].append(self.splines[i]['y'](t_target))
            
            # Point 2
            x_bot_2[i].append(self.splines[i]['x'](self.t['t_plies_bot'][i][i][-1]))
            y_bot_2[i].append(self.splines[i]['y'](self.t['t_plies_bot'][i][i][-1]))
            
            # Point 3
            if i > 1:
                x_bot_2[i].append(c_offset[i-1]['x'](t_bot_3[i-1][i-1][0]))
                y_bot_2[i].append(c_offset[i-1]['y'](t_bot_3[i-1][i-1][0]))
                
            else:
                t_target = splineIntersection(spline=c_offset[i],
                    line=self.guides['line_overlap_offset'][i-1], u0=t_bot_3[i][i-1][0])
                
                x_bot_2[i].append(c_offset[i-1]['x'](t_target))
                y_bot_2[i].append(c_offset[i-1]['y'](t_target))
                
            # Point 4
            x_bot_2[i].append(c_offset[i-1]['x'](t_bot_3[i][i][0]))
            y_bot_2[i].append(c_offset[i-1]['y'](t_bot_3[i][i][0]))
            
            # Repeating Point 1 to make closed shape
            x_bot_2[i].append(x_bot_2[i][0])
            y_bot_2[i].append(y_bot_2[i][0])
        
        x_bot_2 = {ply:[float(x) for x in values] for ply,values in x_bot_2.items()}
        y_bot_2 = {ply:[float(y) for y in values] for ply,values in y_bot_2.items()}
        
        self.lines['bot_2'] = {'x':x_bot_2,'y':y_bot_2}
        
        # Plot
        fig, ax = plt.subplots(figsize=(10,6))
        
        t_plies = [self.t['t_plies_top'], self.t['t_plies_bot']]
        
        cmap = plt.get_cmap('rainbow')
        colours = [cmap(x/(n_plies)) for x in range(n_plies)]
        
        # OVERLAP
        
        for i in range(1,n_plies+1):
            idx_c = list(t_bot_3[i].keys())
            
            # First curve
            ax.plot(c_offset[i-1]['x'](t_bot_3[i][idx_c[0]]),
                    c_offset[i-1]['y'](t_bot_3[i][idx_c[0]]),
                    c = colours[i-1], label = f'Ply {i}')
            
            # Second curve
            ax.plot(c_offset[i]['x'](t_bot_3[i][idx_c[1]]),
                    c_offset[i]['y'](t_bot_3[i][idx_c[1]]),
                    c = colours[i-1], label = None)
            
            # Left edge
            x_edge_left = (c_offset[i-1]['x'](t_bot_3[i][idx_c[0]][0]),
                            c_offset[i]['x'](t_bot_3[i][idx_c[1]][0]))
            y_edge_left = (c_offset[i-1]['y'](t_bot_3[i][idx_c[0]][0]),
                            c_offset[i]['y'](t_bot_3[i][idx_c[1]][0]))
            
            ax.plot(x_edge_left, y_edge_left, label = None, c = colours[i-1])
            
            # Right edge
            x_edge_right = (c_offset[i-1]['x'](t_bot_3[i][idx_c[0]][-1]),
                            c_offset[i]['x'](t_bot_3[i][idx_c[1]][-1]))
            y_edge_right = (c_offset[i-1]['y'](t_bot_3[i][idx_c[0]][-1]),
                            c_offset[i]['y'](t_bot_3[i][idx_c[1]][-1]))
            
            ax.plot(x_edge_right, y_edge_right, label = None, c = colours[i-1])
        
        # SKIN
        
        for i in range(1,n_plies+1):
            
            for j in range(2):
                    
                idx_c = list(t_plies[j][i].keys())
            
                c1 = self.splines[idx_c[0]]
                c2 = self.splines[idx_c[1]]
                
                ax.plot(c1['x'](t_plies[j][i][idx_c[0]]),
                        c1['y'](t_plies[j][i][idx_c[0]]),
                        label = None, c = colours[i-1])
                
                ax.plot(c2['x'](t_plies[j][i][idx_c[1]]),
                        c2['y'](t_plies[j][i][idx_c[1]]),
                        label = None, c = colours[i-1])
                
                # TE side line
                x_edge_right = (c1['x'](t_plies[j][i][idx_c[0]][0]),
                                c2['x'](t_plies[j][i][idx_c[1]][0]))
                y_edge_right = (c1['y'](t_plies[j][i][idx_c[0]][0]),
                                c2['y'](t_plies[j][i][idx_c[1]][0]))
                
                ax.plot(x_edge_right, y_edge_right, label = None, c = colours[i-1])
                
                # Left edge line
                x_edge_right = (c1['x'](t_plies[j][i][idx_c[0]][-1]),
                                c2['x'](t_plies[j][i][idx_c[1]][-1]))
                y_edge_right = (c1['y'](t_plies[j][i][idx_c[0]][-1]),
                                c2['y'](t_plies[j][i][idx_c[1]][-1]))
                
                ax.plot(x_edge_right, y_edge_right, label = None, c = colours[i-1])
        
        # JIGGLE
        
        for i in range(1,n_plies+1):
            ax.plot(x_bot_2[i],y_bot_2[i],label=None, c=colours[i-1])
        
        # Figure properties
        figProperties(ax=ax, title=f'Jiggle')
        
        self.figs['jiggle'] = fig
        if saveFig:
            fig.savefig(f'Jiggle.png', dpi=800)
        plt.close(fig)
        
    def section_info(self) -> str:
        output = f'Station instance name: {self.name}\n'
        output += f'Parameters: {list(self.parameters.keys())}\n'
        output += f'Guides: {list(self.guides.keys())}\n'
        output += f'Indexes: {list(self.indexes.keys())}\n'
        output += f't-parameters: {list(self.t.keys())}\n'
        output += f'CubicSplines: {list(self.splines.keys())}'
        
        return print(output)

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
                  path=os.path.join(os.getcwd(),'airfoils','NACA63430.txt'),
                #   path=os.path.join(os.getcwd(),'airfoils','circle.txt'),
                  )
    
    # sta = Station(chord=906.8,
    #             twist_angle=6.7,
    #             x_offset=-317.88,
    #             y_offset=50,
    #             z_offset=5000,
    #             y_mirror=True,
    #             path=os.path.join(os.getcwd(),'airfoils','NACA63417.txt'),
    #             )
    
    offset_distance = 1
    n_plies = 8
    saveFig = False
    overlap_target = 44.022#200
    trailing_edge_thickness = 8 # mm
    
    db = Section(station=sta, n_plies=n_plies, ply_thickness=offset_distance,
                 overlap_target=overlap_target,
                 te_thickness=trailing_edge_thickness, saveFig=saveFig)
    
    # db.figs['top_ply'][1]
    db.jiggle(86.71)
