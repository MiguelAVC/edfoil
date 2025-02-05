'''IMPORTANT:
- This needs to be compatible with python 2.'''

# Import libraries
import os
import json
import numpy as np
from abaqusConstants import *

# JSON raw decoder (per section)

def importData(
    filepath
):
    # For now is for just one single section!!!!!
    
    with open(filepath, 'r') as file:
        
        data = json.load(file)
        
    # bot_1 and top_1
    skin = {side:{int(ply):{int(curve):tuple(zip(value_3['x'],value_3['y'])) 
        for curve, value_3 in value_2.items()} for ply, value_2 in 
        value_1.items()} for side, value_1 in data.items() if side[-1] == '1'}
    
    # bot_2
    jigg = {int(ply):tuple(zip(values['x'],values['y'])) for ply, values in 
        data['bot_2'].items()}
    
    # bot_3
    ovlp = {int(ply):{int(curve):tuple(zip(value_3['x'],value_3['y'])) 
        for curve, value_3 in value_2.items()} for ply, value_2 in 
        data['bot_3'].items()}
    
    # bond
    bond = {}
    
    bond[0] = {int(curve):tuple(zip(value['x'],value['y'])) for curve, value in
        data['bond']['0'].items()}
    
    bond[1] = tuple(zip(data['bond']['1']['x'],data['bond']['1']['y']))
    
    # te_spar
    tesp = {}
    
    tesp[0] = {int(ply):tuple(zip(value['x'],value['y'])) for ply, value in 
        data['te_spar']['0']['0'].items()}
    
    tesp[1] = {int(ply):{int(curve):tuple(zip(value_2['x'],value_2['y'])) for 
        curve, value_2 in value_1.items()} for ply, value_1 in data['te_spar']['0']['1'].items()}
        
    tesp[2] = {int(ply):tuple(zip(value['x'],value['y'])) for ply, value in 
        data['te_spar']['1']['0'].items()}
    
    tesp[3] = {int(ply):{int(curve):tuple(zip(value_2['x'],value_2['y'])) for 
        curve, value_2 in value_1.items()} for ply, value_1 in data['te_spar']['1']['1'].items()}
            
    data = {
        'bot':skin['bot_1'], 
        'top':skin['top_1'], 
        'jigg':jigg, 
        'ovlp':ovlp, 
        'tesp':tesp, 
        'bond':bond,
    }
    
    return data

def drawSketch(
    data,
    model = 'Model-1',
):
    
    m = mdb.models[model]
    z = list(data.keys())
    
    for section in z:
        
        name_parts = list(data[section].keys())
        
        for component in name_parts:
            
            if component in ['bot','top','ovlp']:
            
                name_plies = list(data[section][component].keys())
            
                for ply in name_plies:
                    
                    # Sketch name
                    sketch_name = '{0}_{1}_{2}'.format(component, str(ply), str(section))
                    
                    # Create sketch instance
                    m.ConstrainedSketch(name=sketch_name, sheetSize=2000.0)
                    s = m.sketches[sketch_name]
                    pts = data[section][component][ply]
                    
                    # Draw lines
                    s.Spline(points=(pts[0]), constrainPoints=False)
                    s.Spline(points=(pts[1]), constrainPoints=False)
                    s.Line(point1=pts[2][0], point2=pts[2][1])
                    s.Line(point1=pts[3][0], point2=pts[3][1])
                    
            elif component == 'jigg':
                
                name_plies = list(data[section][component].keys())
            
                for ply in name_plies:
                    
                    # Sketch name
                    sketch_name = '{0}_{1}_{2}'.format(component, str(ply), str(section))
                    
                    # Create sketch instance
                    m.ConstrainedSketch(name=sketch_name, sheetSize=2000.0)
                    s = m.sketches[sketch_name]
                    pts = data[section][component][ply]
                    
                    # Draw lines
                    for edge in range(4):
                        
                        s.Line(point1 = pts[edge], point2 = pts[edge+1])
            
            elif component == 'tesp':
                
                tesp_comps = list(data[section][component].keys())
                
                for tesp_comp in tesp_comps:
                    
                    name_plies = list(data[section][component][tesp_comp].keys())
                    
                    for ply in name_plies:
                        
                        # Sketch name
                        sketch_name = '{0}_{1}_{2}_{3}'.format(component, str(tesp_comp), str(ply), str(section))
                        
                        # Create sketch instance
                        m.ConstrainedSketch(name=sketch_name, sheetSize=2000.0)
                        s = m.sketches[sketch_name]
                        pts = data[section][component][tesp_comp][ply]
                        
                        if tesp_comp % 2 == 0:
                            
                            for edge in range(4):
                                
                                s.Line(point1 = pts[edge], point2 = pts[edge+1])
                        
                        elif tesp_comp % 2 != 0:
                            
                            s.Spline(points=(pts[0]), constrainPoints=False)
                            s.Spline(points=(pts[1]), constrainPoints=False)
                            s.Line(point1=pts[2][0], point2=pts[2][1])
                            s.Line(point1=pts[3][0], point2=pts[3][1])
                
            elif component == 'bond':
                
                bond_comps = list(data[section][component].keys())
                
                for bond_comp in bond_comps:
                    
                    # Sketch name
                    sketch_name = '{0}_{1}_{2}'.format(component, str(bond_comp), str(section))
                    
                    # Create sketch instance
                    m.ConstrainedSketch(name=sketch_name, sheetSize=2000.0)
                    s = m.sketches[sketch_name]
                    pts = data[section][component][bond_comp]
                    
                    if bond_comp == 0:
                        
                        s.Spline(points=(pts[0]), constrainPoints=False)
                        s.Spline(points=(pts[1]), constrainPoints=False)
                        s.Line(point1=pts[2][0], point2=pts[2][1])
                        s.Line(point1=pts[3][0], point2=pts[3][1])
                        
                    elif bond_comp == 1:
                        
                        for edge in range(4):
                            
                            s.Line(point1=pts[edge], point2=pts[edge+1])
                
            else:
                print('WARNING: Unrecognised component.')

def createParts(
    data,
    model = 'Model-1',
):
    
    m = mdb.models[model]
    z = list(data.keys())
    name_sketches = list(m.sketches.keys())
    name_parts = ['_'.join(x.split('_')[:-1]) for x in name_sketches if x.split('_')[-1] == str(z[0])]
    
    for part in name_parts:
        
        p = m.Part(
            name = part,
            dimensionality = THREE_D,
            type = DEFORMABLE_BODY,
        )
        
        p.DatumAxisByPrincipalAxis(principalAxis=YAXIS)
        p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset = z[0])
        p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset = z[1])
            
        # First sketch
        p.BaseShell(sketch = m.sketches['{0}_{1}'.format(part,str(z[0]))])
        
        # Other sketches
        t = p.MakeSketchTransform(
            sketchPlane = p.datums[3], 
            sketchUpEdge = p.datums[1],
            sketchPlaneSide = SIDE1, 
            sketchOrientation = RIGHT, 
            origin = (0.0,0.0,float(z[1])),
        )
        
        s = m.ConstrainedSketch(
            name        = '__profile__',
            sheetSize   = 2000,
            gridSpacing = 100,
            transform   = t
        )
        
        p.projectReferencesOntoSketch(sketch = s, filter = COPLANAR_EDGES)
        s.retrieveSketch(sketch=m.sketches['{0}_{1}'.format(part,str(z[1]))])
        
        print('sketch retrieved')
        
        p.Shell(
            sketchPlane = p.datums[3],
            sketchUpEdge = p.datums[1],
            sketchPlaneSide = SIDE1,
            sketchOrientation = RIGHT,
            sketch = s,
        )
        
        # Solid loft
        faces = [
            tuple([p.edges[x] for x in j.getEdges()]) for i in range(len(z))
            for j in p.faces if int(j.pointOn[0][2]) == z[i]
        ]
        
        p.SolidLoft(
            loftsections = tuple(faces),
            globalSmoothing = ON,
        )
        
def defMaterials(
    model = 'Model-1',
):
    
    m = mdb.models[model]
    
    # GFRP
    m.Material(name='GFRP', description='E-glass 1600 gcm')
    
    m.materials['GFRP'].Elastic(
        type=ENGINEERING_CONSTANTS, 
        table=(
            (
                48000.0, 
                11000.0, 
                11000.0, 
                0.64, 
                0.64, 
                0.64, 
                4900.0, 
                4900.0, 
                4900.0
            ),
        ),
    )
        
    m.HomogeneousSolidSection(name='GFRP', material='GFRP', thickness=None)
    
    # SPABOND
    mat = m.Material(name='SPABOND')
    mat.Elastic(
        table=(
            (3100.0, 0.3), 
        ),
    )
    
    m.HomogeneousSolidSection(name='SPABOND', material='SPABOND', thickness=None)
    
def assignSecGFRP(
    model = 'Model-1',
):
    
    m = mdb.models[model]
    
    for i in m.parts.keys():
    
        if i[:4] != 'bond':
        
            p = m.parts[i]
        
            # Assign section
            p.SectionAssignment(region=(p.cells[0],), sectionName='GFRP', offset=0.0, 
                offsetType=MIDDLE_SURFACE, offsetField='', 
                thicknessAssignment=FROM_SECTION)
                
            # Material Orientation
            len_faces = [x.getSize(printResults=False) for x in p.faces]
            idx = np.argsort(len_faces)
            face_in = p.faces[idx[-2]:idx[-2]+1]
            face_out = p.faces[idx[-1]:idx[-1]+1]
            
            surf_in = p.Surface(side1Faces=face_in, name='Surf-in')
            surf_out = p.Surface(side1Faces=face_out, name='Surf-out')
            
            p.MaterialOrientation(region=(p.cells[0],), orientationType=DISCRETE, axis=AXIS_1,
                normalAxisDefinition=SURFACE, normalAxisRegion=surf_out, 
                flipNormalDirection=True, normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
                primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
                flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
                angle=0.0, additionalRotationField='', stackDirection=STACK_3)

# Test

if __name__ == '__main__':
    
    # Variables
    sections = [
        'sec1',
        'sec2',
    ]
    
    z = [0, 5250,]
    m = mdb.models['Model-1']
    
    # Load JSON files
    data = {z[i]: importData(filepath=sections[i]+'.json') for i in range(len(sections))}
    n_plies = len(data[0][list(data[0].keys())[0]].keys())
    n_plies_te = len(data[0]['tesp'][0].keys())
    
    # Main functions
    drawSketch(data = data, model = 'Model-1')
    createParts(data = data, model = 'Model-1')
    defMaterials(model = 'Model-1')
    assignSecGFRP(model = 'Model-1')