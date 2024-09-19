import numpy as np

class Airfoil:
    def __init__(self, path:str, name:str) -> None:
        coords = np.genfromtxt(path)
        self.xy = coords.tolist()
        self.n_points = len(coords)
        self.name = name
        
    def update(self,coords:list) -> None:
        self.xy = coords
        self.n_points = len(coords)
    
    def changeName(self, name:str) -> None:
        self.name = name
        
    def exportAirfoil(self) -> None:
        path = './airfoils/' + self.name + '.txt'
        with open(path, 'w') as file:
            for x, y in self.xy:
                line = f'{x} {y}'
                file.write(line + '\n')
        
    def __str__(self) -> str:
        return 'Airfoil Object'
    
        
if __name__ == '__main__':
    # work directory is the root directory /05 App
    path = './coords/NACA63430.txt'
    airfoil = Airfoil(path=path, name='NACA63430')
    path = './coords/circle.txt'
    circle = Airfoil(path=path, name='circle')
    circle.exportAirfoil()