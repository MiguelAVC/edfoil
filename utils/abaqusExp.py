# %% Definitions

# Import libraries
import json
from classes.section import Section

# Bot Sketches
def skinBot(section:Section, name:str):

    bot = {}

    for i in section.t['t_plies_bot'].keys():
        
        idx_curves = list(section.t['t_plies_bot'][i].keys())
        
        # curve 1
        t1 = section.t['t_plies_bot'][i][idx_curves[0]]
        x1 = section.splines[idx_curves[0]]['x'](t1).tolist()
        y1 = section.splines[idx_curves[0]]['y'](t1).tolist()
        
        xy1 = [[x,y] for x,y in zip(x1,y1)]
        
        # curve 2
        t2 = section.t['t_plies_bot'][i][idx_curves[1]]
        x2 = section.splines[idx_curves[1]]['x'](t2).tolist()
        y2 = section.splines[idx_curves[1]]['y'](t2).tolist()
        
        xy2 = [[x,y] for x,y in zip(x2,y2)]
        
        bot[i] = {1:xy1, 2:xy2,
                  3:[xy1[0]] + [xy2[0]], 4:[xy1[-1]] + [xy2[-1]]}
        
    # Save to a JSON file
    with open(f'exports/{name}_bot.json', 'w') as file:
        json.dump(bot, file, indent=4)

# Top Sketches
def skinTop(section:Section, name:str):

    top = {}

    for i in section.t['t_plies_top'].keys():
        
        idx_curves = list(section.t['t_plies_top'][i].keys())
        
        # curve 1
        t1 = section.t['t_plies_top'][i][idx_curves[0]]
        x1 = section.splines[idx_curves[0]]['x'](t1).tolist()
        y1 = section.splines[idx_curves[0]]['y'](t1).tolist()
        
        xy1 = [[x,y] for x,y in zip(x1,y1)]
        
        # curve 2
        t2 = section.t['t_plies_top'][i][idx_curves[1]]
        x2 = section.splines[idx_curves[1]]['x'](t2).tolist()
        y2 = section.splines[idx_curves[1]]['y'](t2).tolist()
        
        xy2 = [[x,y] for x,y in zip(x2,y2)]
        
        top[i] = {1:xy1, 2:xy2,
                  3:[xy1[0]] + [xy2[0]], 4:[xy1[-1]] + [xy2[-1]]}
        
    # Save to a JSON file
    with open(f'exports/{name}_top.json', 'w') as file:
        json.dump(top, file, indent=4)

# %% Example

if __name__ == '__main__':
    
    skinBot(section=db)
    skinTop(section=db)
