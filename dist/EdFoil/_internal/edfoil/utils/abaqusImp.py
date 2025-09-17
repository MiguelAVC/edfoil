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
    n_plies = len(data[list(data.keys())[0]]['top'].keys())
    points = {node:{side:{ply+1:() for ply in range(n_plies)} for side in ['top','bot']} for node in range(4)}
    
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
                
                points[0][side][ply] += ((c[3][0] + (sec,),),)
                points[1][side][ply] += ((c[3][1] + (sec,),),)
                points[2][side][ply] += ((c[4][0] + (sec,),),)
                points[3][side][ply] += ((c[4][1] + (sec,),),)
    
    return points

def createSkinPart(data, points, model='Model-1'):
    
    m = mdb.models[model]
    
    sections = sorted(list(data.keys()))
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
            for wire in range(4):
                vertices = p.vertices.findAt(*points[wire][side][ply])
                wire_object = p.WireSpline(points=tuple(vertices), mergeType=IMPRINT, meshable=ON, smoothClosedSpline=ON)
                
            paths = [tuple(p.getFeatureEdges('Wire-'+str(x+1))) for x in range(4)]
            
            # making sure edje objects inside each path are sorted based on z-coord
            paths_sorted = [sorted(x, key=lambda i:i.pointOn[0][2]) for x in paths]
            
            # 2) create list of tuples with edges belonging to each station
            
            faces = [tuple([p.edges[x] for x in j.getEdges()])
                    for i in range(len(sections)) for j in p.faces
                    if int(j.pointOn[0][2]) == sections[i]]
            
            # 3) loft the whole thing
            p.SolidLoft(loftsections = tuple(faces),
                        paths = tuple(paths_sorted), globalSmoothing = ON)
            
def PartitionSkin(data, part, m=mdb.models['Model-1']):

    # define local variables
    name_parts = m.parts.keys()
    p = m.parts[name_parts[part]]
    name_datums = p.datums.keys()
    
    # partition starting from the root
    for i in range(len(data)-2):
        
        # 1) locate datum plane for reference and for split
        datumPl_ref = p.datums[name_datums[i+1]]
        datumPl_split = p.datums[name_datums[i+2]]
        
        # 2) locate cells past the reference datum plane
        cells = [x for x in p.cells if x.pointOn[0][2]>=datumPl_ref.pointOn[2]]
        
        # 3) partition picked cells
        p.PartitionCellByDatumPlane(cells=tuple(cells),
                                    datumPlane=datumPl_split)

def MeshSkin(part,seedSize=10, m=mdb.models['Model-1']):
    
    # define local variables
    name_parts = m.parts.keys()
    p = m.parts[name_parts[part]]
    
    # seed part
    p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
    
    # identify non structured hex regions
    regions = [x for x in p.cells if p.getMeshControl(x,TECHNIQUE)!=STRUCTURED]
    p.setMeshControls(regions=tuple(regions),elemShape=HEX_DOMINATED)
    
    # generate mesh
    p.generateMesh()
            
def importDatav2(filepath):
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
            
    data = {'bot':skin['bot_1'], 'top':skin['top_1'], 'jigg':jigg, 'ovlp':ovlp, 'tesp':tesp, 'bond':bond}
    
    return 

def genSkinS(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    for i in range(1,9):
        part_name = '{0}_{1}'.format(name, str(i))
        
        m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
        
        s = m.sketches['__profile__']
        
        s.Spline(points=(data[i][0]), constrainPoints=False)
        s.Spline(points=(data[i][1]), constrainPoints=False)
        s.Line(point1=data[i][2][0], point2=data[i][2][1])
        s.Line(point1=data[i][3][0], point2=data[i][3][1])
        
        m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
        
        m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
        
        del mdb.models['Model-1'].sketches['__profile__']
        
def genJiggS(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    for i in range(1,9):
        part_name = '{0}_{1}'.format(name, str(i))
        
        m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
        
        s = m.sketches['__profile__']
        
        for j in range(4):
        
            s.Line(point1=data[i][j], point2=data[i][j+1])
        
        m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
        
        m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
        
        del mdb.models['Model-1'].sketches['__profile__']

def genBond1(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    part_name = name
    
    m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
    
    s = m.sketches['__profile__']
    
    for j in range(4):
    
        s.Line(point1=data[j], point2=data[j+1])
    
    m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
    
    m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
    
    del mdb.models['Model-1'].sketches['__profile__']
        
def genBond2(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    part_name = name
    
    m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
    
    s = m.sketches['__profile__']
    
    s.Spline(points=(data[0]), constrainPoints=False)
    s.Spline(points=(data[1]), constrainPoints=False)
    s.Line(point1=data[2][0], point2=data[2][1])
    s.Line(point1=data[3][0], point2=data[3][1])
    
    m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
    
    m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
    
    del mdb.models['Model-1'].sketches['__profile__']
    
def genTeSp1v1(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    for i in range(1,4):
    
        part_name = '{0}_{1}'.format(name, str(i))
    
        m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
        
        s = m.sketches['__profile__']
        
        for j in range(4):
        
            s.Line(point1=data[i][j], point2=data[i][j+1])
        
        m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
        
        m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
        
        del mdb.models['Model-1'].sketches['__profile__']
        
def genTeSp2v1(data, name, model='Model-1'):
    
    m = mdb.models[model]
    
    for i in range(1,4):
        
        part_name = '{0}_{1}'.format(name,str(i))
    
        m.ConstrainedSketch(name='__profile__', sheetSize=2000.0)
        
        s = m.sketches['__profile__']
        
        s.Spline(points=(data[i][0]), constrainPoints=False)
        s.Spline(points=(data[i][1]), constrainPoints=False)
        s.Line(point1=data[i][2][0], point2=data[i][2][1])
        s.Line(point1=data[i][3][0], point2=data[i][3][1])
        
        m.Part(dimensionality=THREE_D, name=part_name, type= DEFORMABLE_BODY)
        
        m.parts[part_name].BaseSolidExtrude(depth=5250.0, sketch=s)
        
        del mdb.models['Model-1'].sketches['__profile__']

def meshAll(seedSize=10, m=mdb.models['Model-1']):
    
    # define local variables
    for i in m.parts.keys():
        
        p = m.parts[i]
        
        # seed part
        p.seedPart(size=seedSize, deviationFactor=0.1, minSizeFactor=0.1)
        
        # generate mesh
        p.generateMesh()

# %% Example

if __name__ == '__main__':
    data = importData('skin.json')
    points = generateSkinSketches(data)
    createSkinPart(data,points)