'''This python files needs to be compatible with python2 as this will be 
run in the CLI in the Abaqus environment'''

# %% Definitions

# Import libraries
import os
import json
from abaqusConstants import *
# Load JSON files

def importData(filepath):
    # filename = filepath.split('/')[-1][:-5]

    with open(filepath, 'r') as file:
        data = json.load(file)
        
    # Convert most keys to integers and lists of lists to tuples of tuples
    data = {int(section):{side:{int(ply):{int(curve):tuple(tuple(point) for
            point in value_3) for curve, value_3 in value_2.items()} for
            ply, value_2 in value_1.items()} for side, value_1 in 
            value_0.items()} for section, value_0 in data.items()}
    
    return data

def generateSkinSketches(data, model='Model-1'):
    m = mdb.models[model]
    
    # tuple for wire coordinates
    n_plies = len(data[data.keys()[0]]['top'].keys())
    points = {node:{ply:()} for ply in range(n_plies) for node in range(4)}
    
    for sec in sorted(data.keys()):
        for side in data[sec].keys():
            for ply in data[sec][side].keys():
                sketch_name = 'skin_{0}_{1}_{2}'.format(str(sec),side,str(ply))
                s = m.ConstrainedSketch(name = sketch_name,
                                        sheetSize = 2000)
                c = data[sec][side][ply]
                s1 = s.Spline(points = c[1], constrainPoints = False)
                s2 = s.Spline(points = c[2], constrainPoints = False)
                s3 = s.Line(point1=c[3][0], point2=c[3][1])
                s4 = s.Line(point1=c[4][0], point2=c[4][1])
                
                points[0][ply] += (c[3][0] + (sec,),)
                points[1][ply] += (c[3][1] + (sec,),)
                points[2][ply] += (c[4][0] + (sec,),)
                points[3][ply] += (c[4][1] + (sec,),)
    
    return points

def createSkinPart(data, model='Model-1'):
    
    m = mdb.models[model]
    
    sections = list(data.keys())
    sides = list(data[sections[0]].keys())
    plies = list(data[sections[0]][sides[0]].keys())
    
    for side in sides:
        for ply in plies:
            # Part name
            part_name = 'Skin_{0}_{1}'.format(side,str(ply))
            
            # Create part
            p = m.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)
            
            # Create y-axis datum
            y_datum = p.DatumAxisByPrincipalAxis(principalAxis = YAXIS)
            
            for section in sections:
                datumPlane = p.DatumPlaneByPrincipalPlane(principalPlane = XYPLANE,
                                                          offset = section)
                
                t = p.MakeSketchTransform(sketchPlane = p.datums[datumPlane.id], 
                                      sketchUpEdge = p.datums[y_datum.id],
                                      sketchPlaneSide = SIDE1, 
                                      sketchOrientation = RIGHT, 
                                      origin = (0.0,0.0,float(section)))

                # open planar sketch
                s = m.ConstrainedSketch(name        = '__profile__',
                                        sheetSize   = 2000,
                                        gridSpacing = 100,
                                        transform   = t)
                
                p.projectReferencesOntoSketch(sketch = s,
                                            filter = COPLANAR_EDGES)
                
                # retrieve sketch
                sketch_name = 'skin_{0}_{1}_{2}'.format(str(section),side,str(ply))
                
                s.retrieveSketch(sketch=m.sketches[sketch_name])
                
                # generate shell from sketch
                p.Shell(sketchPlane       = p.datums[datumPlane.id],
                        sketchUpEdge      = p.datums[y_datum.id],
                        sketchPlaneSide   = SIDE1,
                        sketchOrientation = RIGHT,
                        sketch            = s)
                
                del m.sketches['__profile__']
                
    # Draw wires

# %% Example

# if __name__ == '__main__':
#     blade = importData('exports/blade.json')
#     generateSkinSketches(blade)
