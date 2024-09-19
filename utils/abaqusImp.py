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
        
    # Convert all keys to integers and lists of lists to tuples of tuples
    data = {int(outer_key): {int(inner_key): tuple(tuple(item) for 
            item in value) for inner_key, value in inner_dict.items()} for
            outer_key, inner_dict in data.items()}
    
    return data

def generateSkinSketches(data, prefix):
    m = mdb.models['Model-1']
    
    for i in data.keys():
        s = m.ConstrainedSketch(name = 'skin_' + prefix + '_' + str(i),
                                sheetSize = 2000)
        
        s1 = s.Spline(points = data[i][1], constrainPoints = False)
        s2 = s.Spline(points = data[i][2], constrainPoints = False)
        s3 = s.Line(point1=data[i][3][0], point2=data[i][3][1])
        s4 = s.Line(point1=data[i][4][0], point2=data[i][4][1])

# %% Example

if __name__ == '__main__':
    bot = importData('exports/bot.json')
    top = importData('exports/top.json')
    
    generateSkinSketches(bot, 'bot')
    generateSkinSketches(top, 'top')
