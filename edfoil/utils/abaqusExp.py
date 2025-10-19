'''
Export cloud points to a JSON format.

:Note: This module needs further improvement and testing as it is only working for skin plies.
'''

# %% Definitions

# Import libraries
import json
from edfoil.classes.section import Section

# Bot Sketches
def skinBot(section:Section) -> dict:

    '''
    Extract bottom skin ply points from a Section object.
    
    :param section: Section object containing skin ply data.
    :type section: Section
    
    :returns: Dictionary of bottom skin ply points.
    :rtype: dict
    '''

    bot = {}

    for i in section.t['bot_plies'].keys():
        
        idx_curves = list(section.t['bot_plies'][i].keys())
        
        # curve 1
        t1 = section.t['bot_plies'][i][idx_curves[0]]
        x1 = section.splines[idx_curves[0]]['x'](t1).tolist()
        y1 = section.splines[idx_curves[0]]['y'](t1).tolist()
        
        xy1 = [[x,y] for x,y in zip(x1,y1)]
        
        # curve 2
        t2 = section.t['bot_plies'][i][idx_curves[1]]
        x2 = section.splines[idx_curves[1]]['x'](t2).tolist()
        y2 = section.splines[idx_curves[1]]['y'](t2).tolist()
        
        xy2 = [[x,y] for x,y in zip(x2,y2)]
        
        bot[i] = {1:xy1, 2:xy2,
                  3:[xy1[0]] + [xy2[0]], 4:[xy1[-1]] + [xy2[-1]]}
        
    return bot

# Top Sketches
def skinTop(section:Section) -> dict:

    '''
    Extract top skin ply points from a Section object.
    
    :param section: Section object containing skin ply data.
    :type section: Section
    
    :returns: Dictionary of top skin ply points.
    :rtype: dict
    '''

    top = {}

    for i in section.t['top_plies'].keys():
        
        idx_curves = list(section.t['top_plies'][i].keys())
        
        # curve 1
        t1 = section.t['top_plies'][i][idx_curves[0]]
        x1 = section.splines[idx_curves[0]]['x'](t1).tolist()
        y1 = section.splines[idx_curves[0]]['y'](t1).tolist()
        
        xy1 = [[x,y] for x,y in zip(x1,y1)]
        
        # curve 2
        t2 = section.t['top_plies'][i][idx_curves[1]]
        x2 = section.splines[idx_curves[1]]['x'](t2).tolist()
        y2 = section.splines[idx_curves[1]]['y'](t2).tolist()
        
        xy2 = [[x,y] for x,y in zip(x2,y2)]
        
        top[i] = {1:xy1, 2:xy2,
                  3:[xy1[0]] + [xy2[0]], 4:[xy1[-1]] + [xy2[-1]]}
        
    return top

# Section

def skinSection(section:Section) -> dict:
    
    '''
    Join top and bottom skin ply points into a section dictionary.
    
    :param section: Section object containing skin ply data.
    :type section: Section
    
    :returns: Dictionary with top and bottom skin ply points.
    :rtype: dict
    '''
    
    sec = {'top':skinTop(section=section), 'bot':skinBot(section=section)}
    return sec

# Skin Part

def skinPart(sections:dict, path:str, filename:str='skin') -> None:
    
    '''
    Writes skin section data to a JSON file.
    
    :param sections: Dictionary containing section data.
    :type sections: dict
    
    :param path: Path to save the JSON file.
    :type path: str
    
    :param filename: Name of the JSON file without extension. Defaults to 'skin'.
    :type filename: str, optional
    
    :returns: None.
    :rtype: None
    '''
    
    # Save to a JSON file
    with open(f'{path}/{filename}.json', 'w') as file:
        json.dump(sections, file, indent=4)

# %% Example

if __name__ == '__main__':
    
    # TODO: create Section objects instead of loading JSONs
    
    with open('tests/blade_0/abaqusExp/bot.json','r') as file:
        bot = json.load(file)
    with open('tests/blade_0/abaqusExp/top.json','r') as file:
        top = json.load(file)
        
    sec_2000 = skinSection(top,bot)
    sec_3000 = skinSection(top,bot)
    
    skinPart(sec_2000,sec_3000,sections=[2000,3000])