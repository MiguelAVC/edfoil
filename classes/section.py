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
from shapely import Polygon

from utils.utils import (splineConstructor, lineConstructor, skinOverlapLocator,
                         splineIntersection, trailingEdgeThickness, progressTime)
from classes.station import Station

# functions
def figProperties(ax,
                  title:str,
                  xlabel:str ='x [-]',
                  ylabel:str ='y [-]',
                  labelsize:str ='large',
                  legend:bool = True,
                  ) -> None:
    
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

def reorder_coordinates(polygon:Polygon, reference_point:list[float,float]):
    
    coords = list(polygon.exterior.coords)
    
    # Find the closest point in the buffer to the reference point
    distances = [np.linalg.norm(np.array(c) - np.array(reference_point)) for c in coords]
    min_index = np.argmin(distances)
    
    # Only reorder if the closest point is not already the first coordinate
    if min_index != 0:
        reordered_coords = coords[min_index:] + coords[:min_index]
        return reordered_coords
    else:
        # If the first coordinate is already the closest, return the original coordinates
        return coords

# Main Class
@progressTime
class Section:
    def __init__(self,
                 station:Station,
                 n_plies:int,
                 ply_thickness:float,
                 overlap_target:float,
                 te_thickness:float = 8,
                 bond_thickness:float = 1,
                 genFig:bool = True,
                 saveFig:bool = False,
                 tolerance:int = 6, # Tolerance for decimal places ACIS
                ) -> None:
        
        # Parameters
        self.parameters = {'n_plies': n_plies,
                           'ply_thickness': ply_thickness,
                           'overlap_target': overlap_target,
                           'te_thickness': te_thickness,
                           'bond_thickness': bond_thickness,
                           'saveFig': saveFig,
                           'base_airfoil': station.airfoil,
                           'z':station.parameters['offset'][2],
                           'twist_angle': station.parameters['twist_angle'],
                           'isCircle': station.parameters['isCircle']
                           }
        
        # self.splines = {} defined later
        self.points = {}
        self.guides = {}
        self.indexes = {}
        self.indexes['ply_cut_bot'] = {}
        self.indexes['ply_cut_top'] = {}
        
        self.t = {x:{} for x in ['bot_ref','bot_splines','bot_plies',
                                 'top_ref','top_splines','top_plies']}
        
        self.figs = {}
        self.name = 'skin_' + str(station.parameters['offset'][2])
        
        # Colormap
        cmap = plt.get_cmap('rainbow')
        self.parameters['colours'] = [cmap(x/(n_plies)) for x in range(n_plies)]
        
        # Offset curves
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
        self.guides['chord'] = chord_line
        
        # Splines
        splines = {x:splineConstructor(curves_offset[x]) for x in range(n_plies+1)}
        self.splines = splines
        
        # Index LE
        idx_LE = {x:round(splineIntersection(spline = splines[x],
            line =chord_line, u0 = 21),tolerance) for x in range(n_plies+1)}
        self.indexes['LE'] = idx_LE
        
        # Full skin graph
        if genFig:
            
            fig, ax = plt.subplots(figsize=(10,6))

            for i in range(n_plies+1):
                
                t = np.arange(0,len(splines[i]['x'].x))
                
                ax.plot(splines[i]['x'](t),splines[i]['y'](t),
                    label = f'Curve {i}', linewidth = 0.5)
                
                ax.scatter(splines[i]['x'](idx_LE[i]),splines[i]['y'](idx_LE[i]), 
                    label = None, marker = 'x', s = 0.5)
                
            figProperties(ax = ax, title = f'Full Skin - {n_plies} plies')
            
            self.figs['section'] = fig
            
            if saveFig:
                fig.savefig('skin.png', dpi = 800)
            plt.close(fig)
        
        # Split in overlap
        if station.parameters['isCircle']:
            
            idx_olp_sta = {x:{0:idx_LE[x]} for x in range(n_plies+1)}
            idx_top_sta = {x:idx_LE[x] for x in range(n_plies+1)}
            overlap_line = chord_line
            self.indexes['olp_sta'] = idx_olp_sta
            self.indexes['top_sta'] = idx_top_sta
            
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
            self.guides['overlap_offset'] = {}
            idx_olp_sta = {}
            idx_top_sta = {i:splineIntersection(spline = splines[i], 
                line = overlap_line, u0 = idx_LE[i]) for i in range(n_plies+1)}

            # Cut all other lines at this point
            for i in range(n_plies+1):
                
                idx_olp_sta[i] = {}
                
                # +1 here is constant for now (bonding thickness)
                x0 = (ply_thickness * i + bond_thickness) * np.cos(overlap_line['nor']) + overlap_line['p'][0]
                y0 = (ply_thickness * i + bond_thickness) * np.sin(overlap_line['nor']) + overlap_line['p'][1]
                p0 = tuple([x0, y0])
                
                offset_olp_line = lineConstructor(p0 = p0, ang = overlap_line['tan'])
                self.guides['overlap_offset'][i] = offset_olp_line
                
                idx_olp_sta[i][0] = splineIntersection(spline = splines[i],
                    line = self.guides['overlap_offset'][0], u0 = idx_LE[i])
                
                if i < n_plies:
                    
                    idx_olp_sta[i][1] = splineIntersection(spline = splines[i+1],
                        line = self.guides['overlap_offset'][0], u0 = idx_LE[i+1])
                
            # Store variables
            self.guides['overlap_start'] = overlap_line
            self.indexes['olp_sta'] = idx_olp_sta
            self.indexes['top_sta'] = idx_top_sta
        
        # Bottom skin t-parameter
        
        for i in range(n_plies+1):
            
            t = np.arange(int(np.ceil(idx_olp_sta[i][0]))).tolist()
            
            if idx_olp_sta[i][0] % int(idx_olp_sta[i][0]) != 0:
                t += [idx_olp_sta[i][0]]
                
            self.t['bot_ref'][i] = t
        
        # Bottom skin FIGURE
        
        if genFig:
            
            fig, ax = plt.subplots(figsize=(10,6))
            
            for i in range(n_plies+1):
                
                t = self.t['bot_ref'][i]
                
                ax.plot(splines[i]['x'](t),splines[i]['y'](t), 
                        label = f'Curve {i}', linewidth = 0.5)
                
            y_line = np.arange(ax.get_ylim()[0], ax.get_ylim()[1])
            x_line = (y_line - overlap_line['b']) / overlap_line['m']
            
            ax.plot(x_line, y_line, label='Skin Overlap', lw=0.5)
            
            figProperties(ax=ax, title='Bottom Skin')
            
            self.figs['bottom'] = fig
            
            if saveFig:
                
                fig.savefig('bottom_skin.png',dpi=800)
                
            plt.close(fig)
        
        # Bot - Trailing Edge Cut
        
        if station.parameters['isCircle']:
            
            idx_te_bot = {x:0 for x in range(n_plies+1)}
            te_line = lineConstructor(p0 = (splines[0]['x'](0),
                splines[0]['y'](0)), ang = chord_line['nor'])
        
        else:
            
            # Cut trailing edge
            idx_TE_bot, idx_TE_top = trailingEdgeThickness(
                d_target = te_thickness, spline = splines[0])
            
            te_line = lineConstructor(
                p0 = (splines[0]['x'](idx_TE_bot), splines[0]['y'](idx_TE_bot)),
                p1 = (splines[0]['x'](idx_TE_top), splines[0]['y'](idx_TE_top)))
            
            idx_te_bot = {x:splineIntersection(spline = splines[x],
                line = te_line) for x in range(n_plies+1)}
        
        # Store variables
        self.guides['TE'] = te_line
        

        for i in range(n_plies+1):
            
            if idx_te_bot[i] == None or idx_te_bot[i] == 0:
                idx_te_bot[i] = 0
                t = []
            else:
                t = [idx_te_bot[i]]
            
            t += np.arange(np.ceil(idx_te_bot[i]),np.ceil(idx_olp_sta[i][0])).tolist()
            t += [idx_olp_sta[i][0]]
            
            self.t['bot_splines'][i] = t
            
        # Store variables
        self.indexes['te_bot'] = idx_te_bot
            
        # Bottom graph with te trimmed
        
        if genFig:
            
            fig, ax = plt.subplots(figsize=(10,6))
            
            for i in range(n_plies+1):
                
                t = self.t['bot_splines'][i]
                x_curve = splines[i]['x'](t)
                y_curve = splines[i]['y'](t)

                ax.plot(x_curve, y_curve, label = f'Curve {i}', linewidth = 0.5)
                
            x_lims = ax.get_xlim()
            y_lims = ax.get_ylim()

            # Overlap line plot
            y_line = np.arange(y_lims[0],y_lims[1])
            x_line = (y_line - overlap_line['b']) / overlap_line['m']
            ax.plot(x_line, y_line, 'r--', label = 'Skin Overlap', lw = 0.3)

            # TE line plot
            y_line = np.arange(y_lims[0],y_lims[1])
            x_line = (y_line - te_line['b']) / te_line['m']
            ax.plot(x_line, y_line, 'r--', label = 'TE cut', lw = 0.3)

            # Figure properties
            figProperties(ax = ax, title = 'Bottom Skin after leading edge trim')
            ax.set_xlim(x_lims)
            ax.set_ylim(y_lims)

            self.figs['bottom_trim'] = fig
            
            if saveFig:
                
                fig.savefig('bottom_skin_2.png',dpi=800)
                
            plt.close(fig)
        
        # Individual TE trim for plies
        
        if station.parameters['isCircle']:
            
            self.indexes['ply_cut_bot'] = {}
            
        else:
            
            for i in range(n_plies-1,-1,-1):
                
                dx = splines[i]['x'](idx_te_bot[i]) - splines[i+1]['x'](idx_te_bot[i+1])
                dy = splines[i]['y'](idx_te_bot[i]) - splines[i+1]['y'](idx_te_bot[i+1])
                beta = np.arctan2(dy,dx)
                alpha = te_line['tan']

                d = np.sqrt(dx**2 + dy**2) * np.sin(beta - alpha)

                if np.abs(d) > 0.5 * ply_thickness:
                    
                    # print(f'Curve {i} does need trim.')
                    
                    line_cut = lineConstructor(p0 = (splines[i+1]['x'](idx_te_bot[i+1]),
                        splines[i+1]['y'](idx_te_bot[i+1])), ang = te_line['tan'])
                    
                    self.indexes['ply_cut_bot'][i] = splineIntersection(
                        spline = splines[i], line = line_cut, u0 = idx_te_bot[i])
                
        # Ply curves
        t_plies_bot = {}
        
        for i in range(n_plies):
            
            t_plies_bot[i+1] = {}
            
            if i not in self.indexes['ply_cut_bot'].keys():
                
                t_plies_bot[i+1][i] = self.t['bot_splines'][i]
                
            else:
                
                t_plies_bot[i+1][i] = [self.indexes['ply_cut_bot'][i]] + \
                    [x for x in self.t['bot_splines'][i] if
                     x > self.indexes['ply_cut_bot'][i]]
                
            if station.parameters['isCircle']:
            
                t_plies_bot[i+1][i+1] = self.t['bot_splines'][i+1]
                
            else:
            
                if idx_te_bot[i+1] == 0:
                    
                    t = []
                    
                else:
                    
                    t = [idx_te_bot[i+1]]
                
                t += np.arange(np.ceil(idx_te_bot[i+1]), np.ceil(idx_olp_sta[i][1])).tolist()
                t += [idx_olp_sta[i][1]]
                
                t_plies_bot[i+1][i+1] = t
        
        # Store variables
        self.t['bot_plies'] = t_plies_bot
            
        # Generate ply points
        pts_bot_1 = {}
        
        for i in range(1,n_plies+1):
            
            idx_curves = list(t_plies_bot[i].keys())
            
            c1 = splines[idx_curves[0]]
            c2 = splines[idx_curves[1]]
            
            pts_bot_1[i] = {}
            
            # Outer curve
            pts_bot_1[i][0] = {axis:c1[axis](t_plies_bot[i][idx_curves[0]]) for axis in ['x','y']}
            
            # Inner curve
            pts_bot_1[i][1] = {axis:c2[axis](t_plies_bot[i][idx_curves[1]]) for axis in ['x','y']}
            
            # TE side line
            x_edge_left = (c1['x'](t_plies_bot[i][idx_curves[0]][0]),
                           c2['x'](t_plies_bot[i][idx_curves[1]][0]))
            y_edge_left = (c1['y'](t_plies_bot[i][idx_curves[0]][0]),
                           c2['y'](t_plies_bot[i][idx_curves[1]][0]))
            
            pts_bot_1[i][2] = {'x':x_edge_left, 'y':y_edge_left}
            
            # Left edge line
            x_edge_right = (c1['x'](t_plies_bot[i][idx_curves[0]][-1]),
                            c2['x'](t_plies_bot[i][idx_curves[1]][-1]))
            y_edge_right = (c1['y'](t_plies_bot[i][idx_curves[0]][-1]),
                            c2['y'](t_plies_bot[i][idx_curves[1]][-1]))
            
            pts_bot_1[i][3] = {'x':x_edge_right, 'y':y_edge_right}
                    
        # Store points
        self.points['bot_1'] = pts_bot_1
        
        ### TOP SIDE
        ### -------------------------------------------------------------------
        
        # Top skin t-parameters

        for i in range(n_plies+1):
            
            if idx_top_sta[i] % int(idx_top_sta[i]) != 0:
                t = [idx_top_sta[i]]
            else:
                t = []
                
            t += np.arange(np.ceil(idx_top_sta[i]), splines[i]['u'] + 1).tolist()
            
            self.t['top_ref'][i] = t
            
        if genFig:
        
            fig, ax = plt.subplots(figsize = (10,6))
            
            for i in range(n_plies+1):
                
                t = self.t['top_ref'][i]
                
                ax.plot(splines[i]['x'](t), splines[i]['y'](t), label = f'Curve {i}')
                
            figProperties(ax = ax, title = 'Before trailing edge cut')
            
            self.figs['top'] = fig
            
            if saveFig:
                
                fig.savefig('top.png', dpi = 800)
                
            plt.close(fig)
                
        # Trailing edge cut
        if station.parameters['isCircle']:
            
            idx_te_top = {x:None for x in range(n_plies+1)}
        
        else:
            
            idx_te_top = {x:splineIntersection(spline = splines[x],
                line = te_line, u0 = idx_top_sta[i]) for x in range(n_plies+1)}
        

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
            
            self.t['top_splines'][i] = t
        
        if genFig:
        
            fig, ax = plt.subplots(figsize = (10,6))
            
            for i in range(n_plies+1):
                
                t = self.t['top_splines'][i]
                
                ax.plot(splines[i]['x'](t), splines[i]['y'](t), label = f'Curve {i}')
            
            figProperties(ax = ax, title = 'After trailing edge cut')
            
            self.figs['top_trim'] = fig
            
            if saveFig:
                
                fig.savefig('top_trim.png', dpi = 800)
                
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

                if np.abs(d) > 0.5 * ply_thickness:
                    
                    # print(f'Curve {i} trimmed.')
                    
                    line_cut = lineConstructor(p0 = (splines[i+1]['x'](idx_te_top[i+1]),
                        splines[i+1]['y'](idx_te_top[i+1])), ang = te_line['tan'])
                    
                    self.indexes['ply_cut_top'][i] = splineIntersection(
                        spline = splines[i], line = line_cut, u0 = idx_top_sta[i])
        
        # Store variables
        self.indexes['idx_te_top'] = idx_te_top
        
        # Store t for each ply
        t_plies_top = {}
        
        for i in range(n_plies):
            
            t_plies_top[i+1] = {}
            
            if i not in self.indexes['ply_cut_top'].keys():
                
                t_plies_top[i+1][i] = self.t['top_splines'][i]
                
            else:
                
                t_plies_top[i+1][i] = [x for x in self.t['top_splines'][i] if 
                    x < self.indexes['ply_cut_top'][i]] + [self.indexes['ply_cut_top'][i]]
                
            t_plies_top[i+1][i+1] = self.t['top_splines'][i+1]
            
        # Store variables
        self.t['top_plies'] = t_plies_top
        
        # Generate top plies
        pts_top_1 = {}
        
        for i in range(1,n_plies+1):
            
            idx_curves = list(t_plies_top[i].keys())
            
            c1 = splines[idx_curves[0]]
            c2 = splines[idx_curves[1]]
            
            pts_top_1[i] = {}
            
            # Outer curve
            pts_top_1[i][0] = {axis:c1[axis](t_plies_top[i][idx_curves[0]]) for axis in ['x','y']}
            
            # Inner curve
            pts_top_1[i][1] = {axis:c2[axis](t_plies_top[i][idx_curves[1]]) for axis in ['x','y']}
            
            # TE side line
            x_edge_left = (c1['x'](t_plies_top[i][idx_curves[0]][0]),
                           c2['x'](t_plies_top[i][idx_curves[1]][0]))
            y_edge_left = (c1['y'](t_plies_top[i][idx_curves[0]][0]),
                           c2['y'](t_plies_top[i][idx_curves[1]][0]))
            
            pts_top_1[i][2] = {'x':x_edge_left, 'y':y_edge_left}
            
            # Left edge line
            x_edge_right = (c1['x'](t_plies_top[i][idx_curves[0]][-1]),
                            c2['x'](t_plies_top[i][idx_curves[1]][-1]))
            y_edge_right = (c1['y'](t_plies_top[i][idx_curves[0]][-1]),
                            c2['y'](t_plies_top[i][idx_curves[1]][-1]))
            
            pts_top_1[i][3] = {'x':x_edge_right, 'y':y_edge_right}
            
        self.points['top_1'] = pts_top_1
        
    def plotSection(self) -> None:
        
        fig, ax = plt.subplots(figsize = (10,6))
        
        n_plies = self.parameters['n_plies']
        
        cmap = plt.get_cmap('rainbow')
        
        colours = [cmap(x/n_plies) for x in range(n_plies)]
        
        for i in range(1,n_plies+1):
            
            ax.plot(self.points['bot_1'][i][0]['x'], self.points['bot_1'][i][0]['y'],
                label = f'Ply {i}', c = colours[i-1])
            
            ax.plot(self.points['top_1'][i][0]['x'], self.points['top_1'][i][0]['y'],
                label = None, c = colours[i-1])
            
            for j in range(1,4):
                
                ax.plot(self.points['bot_1'][i][j]['x'], self.points['bot_1'][i][j]['y'],
                    label = None, c = colours[i-1])
                ax.plot(self.points['top_1'][i][j]['x'], self.points['top_1'][i][j]['y'],
                    label = None, c = colours[i-1])
            
        figProperties(ax = ax, title = f'Full Section')
        
        self.figs['full'] = fig
        
        if self.parameters['saveFig']:
            
            fig.savefig(f'Section.png', dpi = 800)
            
        plt.close(fig)
            
    def jiggle(self, overlap_dist:float, bond_thickness:float=2.0) -> None:
        
        # Error handling for circular airfoil
        if self.parameters['isCircle']:
            
            return print(f'Method is not implemented for circular airfoils.')
        
        # Variables
        n_plies = self.parameters['n_plies']
        base_spline = self.splines[0]
        
        # Base spline data
        lspl_t = np.arange(0, base_spline['u']+1)
        lspl_x = base_spline['x'](lspl_t)
        lspl_y = base_spline['y'](lspl_t)
        lspl_xy = list(zip(lspl_x,lspl_y))
        
        # Offset base spline
        curve_0 = Polygon(lspl_xy)
        c_offset = {}
        
        for i in range(n_plies+1):
            
            thk = round(self.parameters['ply_thickness']*(i+n_plies) + bond_thickness, 2)
            c_buffer = curve_0.buffer(-thk)
            c_simplified = c_buffer.simplify(tolerance = 0.01)
            c_offset[i] = splineConstructor(np.array(c_simplified.exterior.coords))
        
        # Overlap end guide
        p_olp_sta = self.guides['overlap_start']['p']
        
        u0 = splineIntersection(spline = c_offset[0], 
            line = self.guides['chord'], u0 = 0)
        
        t_target = skinOverlapLocator(d_target = overlap_dist, p0 = p_olp_sta,
            twist_ang = self.parameters['twist_angle'], spline = c_offset[0], u0 = u0)
        
        # Intersection coordinates
        p0 = np.array([c_offset[0]['x'](t_target,0),
                       c_offset[0]['y'](t_target,0)])
        
        p1 = p0 + np.array([-c_offset[0]['y'](t_target,1),
                            c_offset[0]['x'](t_target,1)])
        
        line_olp_end = lineConstructor(p0 = tuple(p0), p1 = tuple(p1))
        self.guides['overlap_end'] = line_olp_end
        
        # Finding t-parameter (per ply)
        t_target = {}
        
        for i in range(1, n_plies+1):
            
            t_target[i] = {}
            
            line_start = self.guides['overlap_offset'][i]
            line_end = line_olp_end
            
            # First curve of ply
            u0 = splineIntersection(spline = c_offset[i-1],
                line = self.guides['chord'], u0 = 0)
            
            t_target[i][i-1] = {}
            t_target[i][i-1][0] = splineIntersection(spline = c_offset[i-1], 
                line = line_start, u0 = u0)
            t_target[i][i-1][1] = splineIntersection(spline = c_offset[i-1],
                line = line_end, u0 = t_target[i][i-1][0])
            
            # Second curve of ply
            u0 = splineIntersection(spline = c_offset[i],
                line = self.guides['chord'], u0 = 0)
            
            t_target[i][i] = {}
            t_target[i][i][0] = splineIntersection(spline = c_offset[i],
                line = line_start, u0 = u0)
            t_target[i][i][1] = splineIntersection(spline = c_offset[i],
                line = line_end, u0 = t_target[i][i][0])
            
        # Create t-parameter list for each ply
        t_bot_3 = {}
        
        for i in range(1, n_plies+1):
            
            t_bot_3[i] = {}
            
            for j in list(t_target[i].keys()):
                
                if t_target[i][j][0] % int(t_target[i][j][0]) == 0:
                    
                    t_bot_3[i][j] = []
                    
                else:
                    
                    t_bot_3[i][j] = [float(t_target[i][j][0])]
                
                t_bot_3[i][j] += np.arange(np.ceil(t_target[i][j][0]),np.ceil(t_target[i][j][1])).tolist()
                t_bot_3[i][j] += [float(t_target[i][j][1])]
        
        self.t['bot_3'] = t_bot_3
        
        # Jiggle PART 2 (Vertical part)
        x_bot_2 = {}
        y_bot_2 = {}
        
        for i in range(1, n_plies+1):
            
            x_bot_2[i] = []
            y_bot_2[i] = []
            
            # Point 1
            t_target = splineIntersection(spline=self.splines[i], 
                line=self.guides['overlap_offset'][i], u0=self.indexes['LE'][i])
            
            x_bot_2[i].append(self.splines[i]['x'](t_target))
            y_bot_2[i].append(self.splines[i]['y'](t_target))
            
            # Point 2
            t_target = splineIntersection(spline=self.splines[i], 
                line=self.guides['overlap_offset'][i-1], u0=self.indexes['LE'][i])
            
            x_bot_2[i].append(self.splines[i]['x'](t_target))
            y_bot_2[i].append(self.splines[i]['y'](t_target))
            
            # Point 3
            if i > 1:
                
                x_bot_2[i].append(c_offset[i-1]['x'](t_bot_3[i-1][i-1][0]))
                y_bot_2[i].append(c_offset[i-1]['y'](t_bot_3[i-1][i-1][0]))
                
            else:
                
                t_target = splineIntersection(spline=c_offset[i-1],
                    line=self.guides['overlap_offset'][i-1], u0=t_bot_3[i][i-1][0])
                
                x_bot_2[i].append(c_offset[i-1]['x'](t_target))
                y_bot_2[i].append(c_offset[i-1]['y'](t_target))
                
            # # Point 4
            x_bot_2[i].append(c_offset[i-1]['x'](t_bot_3[i][i-1][0]))
            y_bot_2[i].append(c_offset[i-1]['y'](t_bot_3[i][i-1][0]))
            
            # Repeating Point 1 to make closed shape
            x_bot_2[i].append(x_bot_2[i][0])
            y_bot_2[i].append(y_bot_2[i][0])
        
        x_bot_2 = {ply:[float(x) for x in values] for ply,values in x_bot_2.items()}
        y_bot_2 = {ply:[float(y) for y in values] for ply,values in y_bot_2.items()}
        
        self.points['bot_2'] = {'x':x_bot_2,'y':y_bot_2}
        
        # BOT_3 - OVERLAP
        pts_bot_3 = {}
        
        for i in range(1, n_plies+1):
            
            idx_c = list(t_bot_3[i].keys())
            pts_bot_3[i] = {}
            
            # First curve
            pts_bot_3[i][0] = {axis:c_offset[i-1][axis](t_bot_3[i][idx_c[0]]) for axis in ['x','y']}
            
            # Second curve
            pts_bot_3[i][1] = {axis:c_offset[i][axis](t_bot_3[i][idx_c[1]]) for axis in ['x','y']}
            
            # Left edge
            x_edge_left = (c_offset[i-1]['x'](t_bot_3[i][idx_c[0]][0]),
                            c_offset[i]['x'](t_bot_3[i][idx_c[1]][0]))
            y_edge_left = (c_offset[i-1]['y'](t_bot_3[i][idx_c[0]][0]),
                            c_offset[i]['y'](t_bot_3[i][idx_c[1]][0]))
            
            pts_bot_3[i][2] = {'x':x_edge_left, 'y':y_edge_left}
            
            # Right edge
            x_edge_right = (c_offset[i-1]['x'](t_bot_3[i][idx_c[0]][-1]),
                            c_offset[i]['x'](t_bot_3[i][idx_c[1]][-1]))
            y_edge_right = (c_offset[i-1]['y'](t_bot_3[i][idx_c[0]][-1]),
                            c_offset[i]['y'](t_bot_3[i][idx_c[1]][-1]))
            
            pts_bot_3[i][3] = {'x':x_edge_right, 'y':y_edge_right}
            
        self.points['bot_3'] = pts_bot_3
        
        # Modify BOT_1
        t_bot_1 = {}
        pts_bot_1 = {}
        
        for i in range(1, n_plies+1):
            t_bot_1[i] = {}
            pts_bot_1[i] = {}
            
            for j in [i-1, i]:
            
                t = splineIntersection(spline = self.splines[j],
                    line = self.guides['overlap_offset'][i-1],
                    u0 = self.indexes['LE'][j])
                
                t_bot_1[i][j] = [x for x in self.t['bot_plies'][i][j] if x < t]
                t_bot_1[i][j] += [t]
                
            # XY Points
            # Outer Curve
            pts_bot_1[i][0] = {axis:self.splines[i-1][axis](t_bot_1[i][i-1]) for axis in ['x','y']}
            
            # Inner Curve
            pts_bot_1[i][1] = {axis:self.splines[i][axis](t_bot_1[i][i]) for axis in ['x','y']}
            
            # TE Edge
            pts_bot_1[i][2] = {'x':[pts_bot_1[i][c]['x'][0] for c in range(2)],
                               'y':[pts_bot_1[i][c]['y'][0] for c in range(2)]}
            
            # Jig Edge
            pts_bot_1[i][3] = {'x':[pts_bot_1[i][c]['x'][-1] for c in range(2)],
                               'y':[pts_bot_1[i][c]['y'][-1] for c in range(2)]}
            
        # Updating properties
        self.t['bot_1'] = t_bot_1
        self.points['bot_1'] = pts_bot_1
        
        # Bonding t-parameter
        t_bond = {x:{} for x in range(2)}
        
        t_sta = splineIntersection(spline = self.splines[n_plies],
            line = self.guides['overlap_offset'][0], u0 = self.indexes['LE'][n_plies])
        
        t_end = splineIntersection(spline = self.splines[n_plies],
            line = self.guides['overlap_end'], u0 = t_sta)
        
        t_bond[0][0] = [float(t_sta)] + [float(x) for x in np.arange(
            self.splines[n_plies]['u']) if x > t_sta and x < t_end] + [float(t_end)]
        
        u0 = splineIntersection(spline = c_offset[0], line = self.guides['chord'], u0 = 0)
        
        t_sta = splineIntersection(spline = c_offset[0],
            line = self.guides['overlap_offset'][0], u0 = u0)
        
        t_end = splineIntersection(spline = c_offset[0],
            line = self.guides['overlap_end'], u0 = t_sta)
        
        t_bond[0][1] = [float(t_sta)] + [float(x) for x in np.arange(
            c_offset[0]['u']) if x > t_sta and x < t_end] + [float(t_end)]
        
        pts_bond = {x:{} for x in range(2)}
        
        # Outer Curve
        pts_bond[0][0] = {axis:self.splines[n_plies][axis](t_bond[0][0]) for axis in ['x','y']}
        
        # Inner Curve
        pts_bond[0][1] = {axis:c_offset[0][axis](t_bond[0][1]) for axis in ['x','y']}
        
        # Left Edge
        pts_bond[0][2] = {'x':[pts_bond[0][c]['x'][0] for c in range(2)],
                          'y':[pts_bond[0][c]['y'][0] for c in range(2)]}
        
        # Right Edge
        pts_bond[0][3] = {'x':[pts_bond[0][c]['x'][-1] for c in range(2)],
                          'y':[pts_bond[0][c]['y'][-1] for c in range(2)]}
        
        # Vertical bond
        pts_bond[1] = {axis: [self.points['bot_1'][1][0][axis][-1],
            self.points['top_1'][1][0][axis][0],
            self.points['top_1'][n_plies][1][axis][0],
            pts_bond[0][0][axis][0], self.points['bot_1'][1][0][axis][-1]] 
            for axis in ['x','y']}
        
        # Store variables
        self.points['bond'] = pts_bond
        
        # Plot
        fig, ax = plt.subplots(figsize = (10,6))
        
        colours = self.parameters['colours']
        
        for i in range(1, n_plies+1):
            
            # BOT_2 - JIGGLE
            ax.plot(x_bot_2[i], y_bot_2[i], label = f'Ply {i}', c = colours[i-1])
            
            for j in range(4):
                
                # BOT_1
                ax.plot(pts_bot_1[i][j]['x'], pts_bot_1[i][j]['y'],
                        c = colours[i-1], label = None)            
                
                # BOT_3
                ax.plot(pts_bot_3[i][j]['x'], pts_bot_3[i][j]['y'],
                        c = colours[i-1], label = None)
                
                # TOP_1 
                ax.plot(self.points['top_1'][i][j]['x'],
                    self.points['top_1'][i][j]['y'], label = None, c = colours[i-1])
                
        # BOND
        ax.plot(pts_bond[1]['x'], pts_bond[1]['y'], label = f'Bond', c = 'black')
        
        for i in range(4):
            ax.plot(pts_bond[0][i]['x'], pts_bond[0][i]['y'],
                    c = 'black', label = None)
        
        figProperties(ax = ax, title = f'Jiggle')
        
        self.figs['jiggle'] = fig
        
        if self.parameters['saveFig']:
            
            fig.savefig(f'Jiggle.png', dpi = 800)
            
        plt.close(fig)
        
    def teSpar(self, te_distance:float, thickness:float, flange_distance:float, n_tePlies:float,
        ) -> None:
        
        # Variables
        n_plies = self.parameters['n_plies']
        
        # TE spar guide
        cl = self.guides['chord']
        p = [float(self.splines[0][axis](0)) for axis in ['x','y']]
        
        self.guides['te_spar'] = {}
        
        for i in range(n_tePlies*2 + 1):
            
            p1 = ((i*thickness) + te_distance) * np.array([np.cos(cl['tan']), np.sin(cl['tan'])]) + np.array(p)
            self.guides['te_spar'][i] = lineConstructor(p0 = p1.tolist(), ang = cl['nor'])
        
        # T[0]
        t_b = {part:{side:{} for side in range(2)} for part in range(2)}
        
        # Part [0][0]
        
        ## t_b paremeter bot
        t_b[0][0][0] = splineIntersection(spline = self.splines[n_plies],
            line = self.guides['te_spar'][0], u0 = 0)
        
        for i in range(1,n_tePlies+1):
            
            t_b[0][0][i] = splineIntersection(spline = self.splines[n_plies],
                line = self.guides['te_spar'][i], u0 = t_b[0][0][i-1])
        
        ## t_b parameter top
        t_b[0][1][0] = splineIntersection(spline = self.splines[n_plies],
            line = self.guides['te_spar'][n_tePlies], u0 = self.indexes['LE'][n_plies])
        
        for i in range(1,n_tePlies+1):
            
            t_b[0][1][i] = splineIntersection(spline = self.splines[n_plies],
                line = self.guides['te_spar'][n_tePlies-i], u0 = t_b[0][1][i-1])
        
        # POINTS
        pts_te_spar = {side:{part:{ply:{} for ply in range(1,n_tePlies+1)} for
            part in range(2)} for side in range(2)}
        
        _spline = self.splines[n_plies]
        _bot = [[float(_spline[axis](t_b[0][0][ply])) for axis in ['x','y']] for ply in range(n_tePlies+1)]
        _top = [[float(_spline[axis](t_b[0][1][ply])) for axis in ['x','y']] for ply in range(n_tePlies+1)][::-1]
        
        for i in range(1, n_tePlies+1):
            
            x = [x[0] for x in _bot[i-1:i+1]] + [x[0] for x in _top[i-1:i+1][::-1]]
            y = [x[1] for x in _bot[i-1:i+1]] + [x[1] for x in _top[i-1:i+1][::-1]]
            
            pts_te_spar[0][0][i] = {'x':x+[x[0]], 'y':y+[y[0]]}
        
        # Part [0][1]
        
        ## Offset spline based on number of te plies
        base_spline = self.splines[0]
        
        # Base spline data
        basespl_t = np.arange(0, base_spline['u']+1)
        basespl_x = base_spline['x'](basespl_t)
        basespl_y = base_spline['y'](basespl_t)
        basespl_xy = list(zip(basespl_x,basespl_y))
        
        # Offset base spline
        curve_0 = Polygon(basespl_xy)
        c_offset = {}
        
        for i in range(n_tePlies+1):
            
            thk = round(self.parameters['ply_thickness']*(i+n_plies), 2)
            c_buffer = curve_0.buffer(-thk)
            c_simplified = c_buffer.simplify(tolerance = 0.001)
            coords = reorder_coordinates(polygon = c_simplified, reference_point = p)
            # c_offset[i] = splineConstructor(np.array(c_simplified.exterior.coords))
            c_offset[i] = splineConstructor(coords)
            
        # Find t-parameter close to TE
        t = {}
        
        t[0] = {curve: splineIntersection(spline = c_offset[curve], 
            line = self.guides['te_spar'][n_tePlies], u0 = 0) for curve in range(n_tePlies+1)}
        
        # Find t-parameter at the end of flange
        p1 = ((n_tePlies*2*thickness) + te_distance + flange_distance) * np.array(
            [np.cos(cl['tan']), np.sin(cl['tan'])]) + np.array(p)
        
        self.guides['te_spar_flange'] = lineConstructor(p0 = p1.tolist(), ang = cl['nor'])
        
        t[1] = {curve: splineIntersection(spline = c_offset[curve], 
            line = self.guides['te_spar_flange'], u0 = 0) for curve in range(n_tePlies+1)}
        
        # print(t)
        
        # Generate points for each ply of part[0][1]
        
        for i in range(1, n_tePlies+1):
            
            _a = [t[0][i-1]] + [u for u in np.arange(0,c_offset[i-1]['u']+1) if
                u > t[0][i-1] and u < t[1][i-1]] + [t[1][i-1]]
            
            _b = [t[0][i]] + [u for u in np.arange(0,c_offset[i]['u']+1) if
                u > t[0][i] and u < t[1][i]] + [t[1][i]]
            
            x = c_offset[i-1]['x'](_a).tolist()
            x += c_offset[i]['x'](_b).tolist()[::-1]
            
            # print(f'x_{i}: {x}')
            
            y = c_offset[i-1]['y'](_a).tolist()
            y += c_offset[i]['y'](_b).tolist()[::-1]
            
            # print(f'y_{i}: {y}')
            
            pts_te_spar[0][1][i] = {'x':x+[x[0]], 'y':y+[y[0]]}
        
        # Part [1][0]
        
        # Find t-parameter at bot side (last offset spline from method)
        t = {}
        
        t[0] = [splineIntersection(spline = c_offset[n_tePlies], line = 
            self.guides['te_spar'][line + n_tePlies], u0 = 0) for line in range(n_tePlies+1)]
        
        # Find t-parameter at top side (last offset spline from method)
        t[1] = [splineIntersection(spline = _spline, line = self.guides['te_spar']
            [line + n_tePlies], u0 = self.indexes['LE'][n_plies]) for line in
            range(n_tePlies+1)]
        
        print(t)
        
        # Generate points for part[1][0]
        
        for i in range(1, n_tePlies+1):
            
            x = c_offset[n_tePlies]['x'](t[0][i-1:i+1]).tolist()
            x += self.splines[n_plies]['x'](t[1][i-1:i+1]).tolist()[::-1]
            
            y = c_offset[n_tePlies]['y'](t[0][i-1:i+1]).tolist()
            y += self.splines[n_plies]['y'](t[1][i-1:i+1]).tolist()[::-1]
            
            pts_te_spar[1][0][i] = {'x':x+[x[0]], 'y':y+[y[0]]}
            
        # Part [1][1]
        
        # Find t-parameter at left side (all to the same guide)
        t ={}
        
        _u0 = [splineIntersection(spline = c_offset[curve], line = self.guides['chord'],
            u0 = 0) for curve in range(n_tePlies+1)]
        
        t[0] = {curve: splineIntersection(spline = c_offset[curve], 
            line = self.guides['te_spar_flange'], u0 = _u0[curve]) for curve in range(n_tePlies+1)}
        
        t[1] = {curve: splineIntersection(spline = c_offset[curve], 
            line = self.guides['te_spar'][n_tePlies*2], u0 = t[0][curve]) for curve in range(n_tePlies+1)}
        
        print(t)
        
        # Generate points for part[1][1]
        
        for i in range(1, n_tePlies+1):
            
            _a = [t[0][i-1]] + [u for u in np.arange(0,c_offset[i-1]['u']+1) if
                u > t[0][i-1] and u < t[1][i-1]] + [t[1][i-1]]
            
            _b = [t[0][i]] + [u for u in np.arange(0,c_offset[i]['u']+1) if
                u > t[0][i] and u < t[1][i]] + [t[1][i]]
            
            x = c_offset[i-1]['x'](_a).tolist()
            x += c_offset[i]['x'](_b).tolist()[::-1]
            
            # print(f'x_{i}: {x}')
            
            y = c_offset[i-1]['y'](_a).tolist()
            y += c_offset[i]['y'](_b).tolist()[::-1]
            
            # print(f'y_{i}: {y}')
            
            pts_te_spar[1][1][i] = {'x':x+[x[0]], 'y':y+[y[0]]}
        
        # Store Variables
        self.points['te_spar'] = pts_te_spar
        
        # Plot
        fig, ax = plt.subplots(figsize = (10,6))
        
        colours = self.parameters['colours']
        pts = self.points
        
        for i in range(1, n_plies+1):
            
            # BOT_2 - JIGGLE
            ax.plot(pts['bot_2']['x'][i], pts['bot_2']['y'][i], label = f'Ply {i}', c = colours[i-1])
            
            for j in range(4):
                
                # BOT_1
                ax.plot(pts['bot_1'][i][j]['x'], pts['bot_1'][i][j]['y'],
                        c = colours[i-1], label = None)            
                
                # BOT_3
                ax.plot(pts['bot_3'][i][j]['x'], pts['bot_3'][i][j]['y'],
                        c = colours[i-1], label = None)
                
                # TOP_1 
                ax.plot(pts['top_1'][i][j]['x'],
                    pts['top_1'][i][j]['y'], label = None, c = colours[i-1])
                
        # BOND
        ax.plot(pts['bond'][1]['x'], pts['bond'][1]['y'], label = f'Bond', c = 'black')
        
        for i in range(4):
            
            ax.plot(pts['bond'][0][i]['x'], pts['bond'][0][i]['y'],
                    c = 'black', label = None)
            
        # TE SPAR Part[0]
        for i in range(1, n_tePlies+1):
            
            ax.plot(pts_te_spar[0][0][i]['x'], pts_te_spar[0][0][i]['y'],
                c = 'grey', label = None)
            
            ax.plot(pts_te_spar[0][1][i]['x'], pts_te_spar[0][1][i]['y'],
                c = 'grey', label = None)
            
        # TE SPAR Part[1]
        ax.plot(pts_te_spar[1][0][1]['x'], pts_te_spar[1][0][1]['y'],
                c = 'pink', label = 'TE Spar [1]')
        
        ax.plot(pts_te_spar[1][1][1]['x'], pts_te_spar[1][1][1]['y'],
                c = 'pink', label = None)
        
        for i in range(2, n_tePlies+1):
            
            ax.plot(pts_te_spar[1][0][i]['x'], pts_te_spar[1][0][i]['y'],
                c = 'pink', label = None)
            
            ax.plot(pts_te_spar[1][1][i]['x'], pts_te_spar[1][1][i]['y'],
                c = 'pink', label = None)
        
        figProperties(ax = ax, title = f'TE_Spar')
        
        self.figs['TE_spar'] = fig
        
        if self.parameters['saveFig']:
            
            fig.savefig(f'TE_spar.png', dpi = 800)
            
        plt.close(fig)
        
    def info(self) -> None:
        
        output  = f'Station instance name: {self.name}\n'
        output += f'Parameters: {list(self.parameters.keys())}\n'
        output += f'Guides: {list(self.guides.keys())}\n'
        output += f'Indexes: {list(self.indexes.keys())}\n'
        output += f't-parameters: {list(self.t.keys())}\n'
        output += f'CubicSplines: {list(self.splines.keys())}\n'
        output += f'Points: {list(self.points.keys())}\n'
        output += f'Figures: {list(self.figs.keys())}'
        
        return print(output)

# %% Tests

if __name__ == '__main__':
    
    switch = 3
    
    # Debug (#3)
    if switch == 1:
    
        # Arguments
        sta = Station(chord = 1334,
                      twist_angle = 24.3,
                      x_offset = -474.26,
                      y_offset = 255,
                      z_offset = 1500,
                      y_multiplier = 1.55,
                      y_mirror = True,
                      path = os.path.join(os.getcwd(),'airfoils','NACA63430.txt'),
                      #   path = os.path.join(os.getcwd(),'airfoils','circle.txt'),
                     )
        
        offset_distance = 1
        n_plies = 8
        saveFig = False
        overlap_target = 44.022
        trailing_edge_thickness = 8 # mm
        
        sec = Section(station = sta,
                     n_plies = n_plies,
                     ply_thickness = offset_distance,
                     overlap_target = overlap_target,
                     te_thickness = trailing_edge_thickness,
                     saveFig = saveFig)
        
        sec.jiggle(overlap_dist = 86.71, bond_thickness = 1)
        sec.teSpar(te_distance=140, thickness=1, flange_distance=50, n_tePlies=3)
        # db.figs['jiggle'].show()
    
    # Debug (#8)
    elif switch == 2:
        
        sta = Station(chord = 768.7,
                      twist_angle = 5.2,
                      x_offset = -270.03,
                      y_offset = 25,
                      z_offset = 6000,
                      y_mirror = True,
                      path = os.path.join(os.getcwd(),'airfoils','NACA63416.txt'),
                     )
        
        db = Section(station = sta,
                     n_plies = 8,
                     ply_thickness = 1,
                     overlap_target = 38.1787666667,
                     te_thickness = 8,
                     saveFig = False)
        
        db.jiggle(overlap_dist = 40, bond_thickness = 1)
        # db.figs['jiggle'].show()
    
    # Data from csv 
    elif switch == 3:
        
        data = ['NACA63416',739,4.8,-260,20,6250,1,1,1,False,True]
        data_sec = [8,1,38.178766667,8,1,True,False,6]
        
        sta = Station(chord = data[1],
                      twist_angle = data[2],
                      x_offset = data[3],
                      y_offset = data[4],
                      z_offset = data[5],
                      x_multiplier = data[6],
                      y_multiplier = data[7],
                      z_multiplier = data[8],
                      x_mirror = data[9],
                      y_mirror = data[10],
                      path=os.path.join(os.getcwd(),'airfoils',f'{data[0]}.txt'),
                     )
        
        sec = Section(station = sta,
                      n_plies = data_sec[0],
                      ply_thickness = data_sec[1],
                      overlap_target = data_sec[2],
                      te_thickness = data_sec[3],
                      bond_thickness = data_sec[4],
                      genFig = data_sec[5],
                      saveFig = data_sec[6],
                      tolerance = data_sec[7],
                     )
        
        sec.jiggle(overlap_dist = 40, bond_thickness = 1)
        sec.teSpar(te_distance=140, thickness=1, flange_distance=50, n_tePlies=3)