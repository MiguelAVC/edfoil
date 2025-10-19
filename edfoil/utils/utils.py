# -*- coding: utf-8 -*-
# Created on Thu Jul 11 12:07:16 2024
# @author: s1982685
"""
General utility functions for all classes and modules.

Has 2 functions that require Abaqus.
"""

#%% Import libraries

import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import root_scalar
import sys
import time
import json
# from abaqusConstants import *

#%% ---------------------------------------------------------------------------
# Auxiliary functions
## ----------------------------------------------------------------------------
### Only to generate extra data that might be used multiple times in different
### functions.

# -------------------------------
# 0) Spline construction function
# -------------------------------

# def splineConstructor(*args, names=None):
def splineConstructor(*args, **kwargs): # Py2
    """Creates a spline object for each argument.
    
    Args:
        *args (tuple): Tuple of tuples of x, y coordinates.
        names (list of str, optional): List of custom names for each argument.
    
    Returns:
        dict: Dictionary with 'x','y','u' for each data input.
    """    
    
    def cubicSpline(data):
        x, y = zip(*data)
        u = len(x) - 1
        
        cs_x = CubicSpline(np.arange(len(x)),x)
        cs_y = CubicSpline(np.arange(len(y)),y)
        
        return cs_x, cs_y, u
    
    if len(args) == 1:
        cs_x, cs_y, u = cubicSpline(args[0])
        spline = {'x': cs_x, 'y': cs_y, 'u': u}
        
    else:
        spline = {}
        names = kwargs.get('names', None) # Py2
        
        for i, arg in enumerate(args):
            cs_x, cs_y, u = cubicSpline(arg)
            
            if names and i < len(names):
                key = names[i]
            else:
                key = i + 1
            
            spline[key] = {'x':cs_x, 'y':cs_y, 'u': u}
    
    return spline

# -----------------------------
# 1) Line construction function
# -----------------------------

def lineConstructor(p0, p1 = None, ang = None):
    """Creates a line function based on two points. p1 and ang are mutually 
    exclusive.

    Args:
        p0 (tuple): Tuple of floats with x,y coordinates.
        p1 (tuple, optional): Tuple of floats with x,y coordinates.
        ang (float, optional): Angle in radians.

    Returns:
        dict: Dictionary with slope, intercept, tangent, normal, and p0.
    """
    
    if p1 is not None:
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        
        try:
            m = dy/dx
            b = p1[1] - m * p1[0]
            ang = np.arctan2(dy,dx)
        
        # For vertical lines
        except ZeroDivisionError:
            m = 0
            b = 0
            ang = np.pi/2
            
    elif ang is not None:
        m = np.tan(ang)
        b = p0[1] - m * p0[0]
    
    return {'m':m , 'b':b, 'tan':ang, 'nor':ang+np.pi/2, 'p':p0}

# -----------------------------------
# 2) Curve locator Y (above) function
# -----------------------------------
## To find whether a curve is above or below the chord length
    
def curveLocatorY(line, point):
    """Evaluates if a point is above or below the chord length.

    Args:
        line (dict): line object.
        point (pair of floats): x,y coordinates of curve.

    Returns:
        Boolean: True if point is above and False if point is below.
    """
    
    # handling vertical lines
    if np.abs(line['tan']) == np.pi:
        raise ValueError('Line is vertical, can only compare x value.')
    
    # calculate y-coordinate for the point on the function
    y_curve = line['m'] * point[0] + line['b']
    
    # evaluate if it is under (TRUE if above or on line, FALSE if under)
    return point[1] >= y_curve

# ----------------------------------
# 3) Curve locator X (side) function
# ----------------------------------
## To find whether a curve is right or left of a construction line

def curveLocatorX(line, point):
    """Evaluates if a point is right or left of a line.

    Args:
        line (dict): line object.
        point (pair of floats): x,y coordinates of curve.

    Returns:
        Boolean: True if point is right and False if point is left.
    """
    
    # handling horizontal lines
    if line['tan'] == 0 or np.abs(line['tan']) == np.pi:
        raise ValueError('Line is horizontal, can only compare y value.')
    
    # handling vertical lines
    try:
        x_curve = (point[1] - line['b']) / line['m']
    except ZeroDivisionError:
        x_curve = line['p'][0]
    
    # evaluate y-coordinates (TRUE if right or on line, FALSE if left)
    return point[0] >= x_curve

# -----------------------------------
# 4) Find max y-value on a spline object
# -----------------------------------
## This is needed when playing with Abaqus splines since they don't have points
## TODO IMPORTANT: NEEDS TO BE DEPRECATED EVENTUALLY

def splineYMax(spline):
    
    '''
    Find the maximum y-value on a spline object. (Abaqus API)
    
    :note: This function requires Abaqus environment.
    :note: This function is deprecated and will be removed in future versions.
    '''
    
    y_values = [spline.getPointAtDistance(point=spline.getVertices()[0].coords,
                distance=x,percentage=True)[1] for x in range(101)]
    
    idx_y_max = np.argmax(y_values)
    
    return y_values[idx_y_max]

# ----------------------------
# 5) Sort splines based on length
# ----------------------------
## This is inside a sketch between 2 construction lines using curveLocatorX

def sortSplines(g,line1,line2,chord=False):
    
    '''
    Sort splines between two lines based on their length.
    
    :note: This function requires Abaqus environment.
    
    :param g: Dictionary of geometry objects.
    :type g: dict
    
    :param line1: First construction line object.
    :type line1: dict
    
    :param line2: Second construction line object.
    :type line2: dict
    
    :param chord: If True, uses Y locator (for chord lines). Defaults to False.
    :type chord: bool, optional
    
    :returns: List of sorted spline objects.
    :rtype: list
    '''
    
    # identify splines between the two lines
    if not chord:
        curves = [x for x in g.values() if x.curveType != LINE and
                  curveLocatorX(line1,x.pointOn) and not
                  curveLocatorX(line2,x.pointOn)]
    
    else:
        curves = [x for x in g.values() if x.curveType != LINE and
                  curveLocatorY(line1,x.pointOn) and not
                  curveLocatorX(line2,x.pointOn)]
    
    # get id and length of all curves filtered
    curves_len = np.array([[x.id,x.getSize()] for x in curves])
    
    # sort array in ascending order (first is the smallest spline)
    len_sorted = curves_len[curves_len[:,1].argsort()]
    curves_sorted = [g[x] for x in len_sorted[:,0].astype(int)]
    
    return curves_sorted

# ------------------
# 6) Progress indicator
# ------------------
## Needed as functions takes more than 10mins.

def progressBar(unit,id,iter,total):

    '''
    Display a progress bar in the console.
    
    :note: Tested in the Abaqus console.
    
    :param unit: Unit of the progress (e.g., "Station").
    :type unit: str
    
    :param id: Identifier of the current item.
    :type id: int
    
    :param iter: Current iteration number.
    :type iter: int
    
    :param total: Total number of iterations.
    :type total: int
    
    :returns: None.
    :rtype: None
    
    '''

    padding = len(str(total))
    percentage = (iter+1)*100 / total
    sys.stdout.write('{} {:>{}}: [{}{}] {:.2f}%\n'.
                     format(unit, id, padding, '#'*(iter + 1),
                            ' '*(total-iter-1), percentage))
    sys.stdout.flush()

# ---------------
# 7) JSON encoder
# ---------------

class npEncoder(json.JSONEncoder):
    
    '''
    JSON encoder for numpy data types.
    
    :param obj: Object to encode.
    :type obj: object
    
    :returns: Encoded object.
    :rtype: object
    '''
    
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, CubicSpline):
            return obj(obj.x)
        return super(npEncoder, self).default(obj)


# ------------------
# 8) Backup database
# ------------------

def saveDB(db):
    
    '''
    Save the database to a JSON file.
    
    :note: This function was tested in Abaqus environment.
    :note: This function will be deprecated in future versions.
    
    :param db: Database dictionary.
    :type db: dict
    
    :returns: None.
    :rtype: None
    '''
    
    # Save json file for back up
    filename = 'db_'+time.strftime('%Y-%m-%d_%H-%M', time.localtime()) +'.json'
    file = os.path.join(db['path']['data'], filename)
    with open(file, 'w') as f:
        json.dump(db, f, cls=npEncoder)

# ------------------
# 9) Progress decorator
# ------------------
from functools import wraps

def progressTime(obj):
    
    '''
    Decorator to measure execution time of functions or class initialisations.
    
    :param obj: Function or class to decorate.
    :type obj: function or class
    
    :returns: Decorated function or class.
    :rtype: function or class
    '''
    
    # Don’t alter objects during doc builds
    if os.environ.get("READTHEDOCS") == "True":
        return obj
    
        # Class decorator: wrap __init__, keep the class type intact
    if isinstance(obj, type):
        orig_init = obj.__init__

        @wraps(orig_init)
        def __init__(self, *args, **kwargs):
            t0 = time.perf_counter()
            try:
                return orig_init(self, *args, **kwargs)
            finally:
                dt = (time.perf_counter() - t0) * 1000
                print(f"{obj.__name__} calculated in {dt:.1f} ms.")
        obj.__init__ = __init__
        return obj

    # Function decorator
    @wraps(obj)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return obj(*args, **kwargs)
        finally:
            dt = (time.perf_counter() - t0) * 1000
            print(f"{obj.__name__} function executed in {dt:.1f} ms.")
    return wrapper
    
    # def wrapper(*args,**kwargs):
        
    #     # record the start time
    #     start_time = time.time()
        
    #     # execute the function
    #     result = obj(*args, **kwargs)
        
    #     # calculate time elapsed
    #     elapsed_time = time.time() - start_time
    #     print('- Completed in {:.3f}s.\n'.format(elapsed_time))
        
    #     # save changes to database
    #     # if result is not None:
    #     #     saveDB(db=kwargs['db'])
        
    #     return result
    return wrapper

# ------------------------------
# 10) Line connections identifier
# ------------------------------

def connectedGeometry(objects, ref_coord):
    """Finds all the geometries connected to the reference vertex.

    Args:
        objects (dict): Dictionary with id:(sta,end) coordinates of each line.
        ref_coord (tuple): Tuple of the initial coordinates.

    Returns:
        list: List with keys of the connected geometries.
        tuple: Pair of floats with the open end coordinates.
    """
    
    connected_keys = []
    explorer = []
    # In case no segments are found in the initial coordinate
    idx_current = None
    coord_end = None
    
    # Start with the initial coordinate
    for key, coords in objects.items():
        if ref_coord in coords:
            # Save the geometry index
            connected_keys.append(key)
            # Find if ref_coord is [0] or [1] of the geometry
            idx_current = coords.index(ref_coord)
            # Flag the geometry index and the coord index
            explorer.append((key,idx_current))
            # Save the other coordinate (open end)
            coord_end = coords[1-idx_current]
            break
            
    # Find all connected objects
    while explorer:
        key_geometry_current, idx_current = explorer.pop()
        # current_coords = objects[key_geometry_current]
        
        for key, coords in objects.items():
            # Exclude geometries already found
            if key not in connected_keys:
                # Check if open end coord matches any new geometry
                if coord_end in coords:
                    # Save index of new geometry found
                    connected_keys.append(key)
                    # Find index of coord in geometry [0] or [1]
                    idx_current = coords.index(coord_end)
                    # Flag geometry index and coord index
                    explorer.append((key,idx_current))
                    # Update end coordinate to the unlinked coordinate
                    coord_end = coords[1 - idx_current]
                    # Re-start loop to find other geometry with new open end
                    break
                    
    return connected_keys, coord_end

# ----------------------------
# 11) Skin overlap root finder
# ----------------------------

def skinOverlapLocator(d_target,p0,twist_ang,spline,u0):
    
    '''
    Locate the skin overlap for a given point and twist angle on a spline.
    
    :note: This function is the backbone of the section class.
    
    :param d_target: Target overlap distance.
    :type d_target: float
    
    :param p0: Tuple of floats with x,y coordinates of the point.
    :type p0: tuple
    
    :param twist_ang: Twist angle in degrees.
    :type twist_ang: float
    
    :param spline: Spline object.
    :type spline: dict
    
    :param u0: Minimum parameter value to start searching.
    :type u0: float
    
    :returns: Parameter value on the spline where the overlap occurs.
    :rtype: float
    '''
    
    x0, y0 = p0
    u = spline['u']
    
    def difference(t_val):
        x = spline['x'](t_val)
        y = spline['y'](t_val)
        
        dx = x - x0
        dy = y - y0
        
        beta = np.arctan2(dy,dx)
        alpha = beta + np.radians(twist_ang)
        
        d = np.sqrt(dx**2 + dy**2) * np.cos(alpha)
        
        return d_target - d
    
    # Find the roots (intersection points) of the difference function
    t_range = np.linspace(u0, u, 100)
    
    for i in range(len(t_range) - 1):
        if difference(t_range[i]) * difference(t_range[i + 1]) < 0:
            # There's a sign change between t_range[i] and t_range[i + 1], 
            # refine this interval
            root_result = root_scalar(difference,
                                      bracket=[t_range[i], t_range[i + 1]],
                                      method='brentq')
            
            if root_result.converged:
                return root_result.root

# ---------------
# 12) Trailing edge root finder
# ---------------

# Iterate on u until the sign changes, then find roots for intersection.

def trailingEdgeThickness(d_target,spline):
    
    '''
    Locate the trailing edge thickness for a given distance on a spline.
    
    :param d_target: Target trailing edge distance.
    :type d_target: float
    
    :param spline: Spline object.
    :type spline: dict
    
    :returns: t-value on the spline where the trailing edge thickness occurs.
    :rtype: float
    '''
    
    # Define variables
    distance_target = d_target
    x, y, u = spline.values()
    u1 = np.linspace(0, u/2, num=100)
    u2 = np.linspace(u, u/2, num=100)
    
    # Define the difference function for finding intersections
    def difference(t_val):
        x1 = x(u1[int(t_val)])
        y1 = y(u1[int(t_val)])
        
        x2 = x(u2[int(t_val)])
        y2 = y(u2[int(t_val)])
        
        distance = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        return distance_target - distance
    
    # Find the roots (intersection points) of the difference function
    t_range = np.arange(0,len(u1),dtype=int)
    for i in range(len(u1) - 1):
        # Check for a sign change to identify intervals where roots exist
        if difference(i) * difference(i + 1) < 0:
            # Use the actual u1 values as brackets
            root_result = root_scalar(difference,
                                      bracket=[i, i + 1],
                                      method='brentq')
            
            if root_result.converged:
                # Return the actual parameter value at the root, not the index
                # Use the value in u1 to get the root parameter in terms of u
                root_u1 = u1[int(root_result.root)]
                root_u2 = u2[int(root_result.root)]
                
                return (root_u1, root_u2)

    return None  # If no root is found

# DEPRECATED ################
# def trailingEdgeThickness(d_target,spline1,spline2):
    
#     # Define variables
#     distance_target = d_target
#     x_bot, y_bot, _ = spline1.values()
#     x_top, y_top, u = spline2.values()
    
#     # Define the difference function for finding intersections
#     def difference(t_val):
#         x1 = x_bot(t_val)
#         y1 = y_bot(t_val)
        
#         x2 = x_top(t_val)
#         y2 = y_top(t_val)
        
#         distance = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        
#         return distance_target - distance
    
#     # Find the roots (intersection points) of the difference function
#     t_range = np.linspace(0, u, 100)
#     for i in range(len(t_range) - 1):
#         if difference(t_range[i]) * difference(t_range[i + 1]) < 0:
#             # There's a sign change between t_range[i] and t_range[i + 1], 
#             # refine this interval
#             root_result = root_scalar(difference,
#                                       bracket=[t_range[i], t_range[i + 1]],
#                                       method='brentq')
            
#             if root_result.converged:
#                 return root_result.root
            
# -----------------------------------
# 13) Spline intersection root finder
# -----------------------------------

def splineIntersection(spline,line,u0=0):

    """
    Find the intersection point between a spline and a line.

    :param spline: Spline object.
    :type spline: dict
    
    :param line: Line object defined by slope and intercept.
    :type line: dict
    
    :param u0: Minimum parameter value to start searching. Defaults to 0.
    :type u0: float, optional
    
    :returns: t-value on the spline where the intersection occurs.
    :rtype: float
    """

    # Define variables
    u = spline['u']
    
    def difference(t_val):
        x = spline['x'](t_val)
        y = spline['y'](t_val)
        
        x_line =  (y - line['b']) / line['m']
        
        return x_line - x
    
    # Find the roots (intersection points) of the difference function
    t_range = np.linspace(u0, u, 50)
    
    for i in range(len(t_range) - 1):
        if difference(t_range[i]) * difference(t_range[i + 1]) < 0:
            # There's a sign change between t_range[i] and t_range[i + 1], 
            # refine this interval
            root_result = root_scalar(difference,
                                      bracket=[t_range[i], t_range[i + 1]],
                                      method='brentq')
            
            if root_result.converged:
                return root_result.root
        
        # Send the last t so the spline is plotted fully.
        # elif i == range(len(t_range) - 1):
        #     return i
    
# -----------------------------------
# 14) Cosine spacing function
# -----------------------------------

# Cosine spacing for better point distribution
def cosSpacing(xmin, xmax, n) -> np.ndarray:
    
    '''
    Generate cosine-spaced values for airfoils between xmin and xmax.
    
    :param xmin: Minimum x value.
    :type xmin: float
    
    :param xmax: Maximum x value.
    :type xmax: float
    
    :param n: Number of points to generate.
    :type n: int
    
    :returns: Numpy array of cosine-spaced x values.
    :rtype: np.ndarray
    '''
    
    beta = np.linspace(0, np.pi, n)
    return 0.5 * (xmin + xmax) + 0.5 * (xmax - xmin) * np.cos(beta)