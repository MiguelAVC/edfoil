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

def generateSkinSketches(data):
    m = mdb.models['Model-1']
    
    for sec in data.keys():
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

# %% Example

if __name__ == '__main__':
    blade = importData('exports/blade.json')
    generateSkinSketches(blade)
