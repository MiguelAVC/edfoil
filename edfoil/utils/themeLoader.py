from pathlib import Path
from edfoil.utils.dev import resource_path
import re

class Theme():
    def __init__(self, name="default"):
        self.name = name
        self.template = self.load_template()

    def load_template(self) -> str:
        tpl_path = Path(resource_path('resources/themes/template.qss'))
        return tpl_path.read_text(encoding="utf-8")

    def load_qss(self, path:str=None, sout:bool=False) -> str:

        # Locate theme file
        path = Path(path)
        
        # Turn theme file into a dict of variables
        if not path.exists():
            path = Path('resources/themes/default.qss')
            
        theme = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            # Get values inside quotes with a regex
            match = re.search(r'\"(.*?)\"\s*:\s*\"(.*?)\"', line)
            if match:
                key, val = match.groups()
                # print(f'Key: "{key.strip()}", Value: "{val.strip()}"')
                theme[key.strip()] = val.strip()

        text = self.template
        # Simple placeholder replacement {{TOKEN}}
        for key, val in theme.items():
            text = text.replace(f"{{{{{key}}}}}", val)
        
        self.palette = theme  
        self.qss = text
        
        if sout:
            return self.qss
    
if __name__ == "__main__":
    # One theme
    theme_path = 'resources/themes/default.qss'
    theme = Theme()
    qss = theme.load_qss(theme_path)
    
    # Multiple themes
    theme_folder = resource_path('resources/themes')
    theme_path = Path(theme_folder)
    theme_list = [p.stem for p in theme_path.glob("*.qss") if p.stem != "template"]
    print("Available themes:", theme_list)
    
    themes = {}
    for t in theme_list:
        theme = Theme(t)
        theme_path = theme_path / f"{t}.qss"
        themes[t] = theme.load_qss(theme_path, sout=True)