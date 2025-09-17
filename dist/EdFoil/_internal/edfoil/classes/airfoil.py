import numpy as np
import json
from scipy.interpolate import CubicSpline

class Airfoil:
    def __init__(self, name:str) -> None:
        self.path = None
        self.name = name
        
    def __str__(self) -> str:
        return 'Airfoil Object'
        
    def importCoords(self, path:str) -> None:
        self.path = path
        coords = np.genfromtxt(path)
        self.xy = coords.tolist()
        self.n_points = len(coords)
        
    def update(self,coords:list) -> None:
        self.xy = coords
        self.n_points = len(coords)
    
    def changeName(self, name:str) -> None:
        self.name = name
        
    def exportAirfoil(self, path:str) -> None:
        filepath = path + self.name + '.txt'
        with open(filepath, 'w') as file:
            for x, y in self.xy:
                line = f'{x} {y}'
                file.write(line + '\n')
    
    # NACA 6 series implementation
    def naca6(self, profile:str, path:str, n_points:int) -> dict:
        """
        Loads NACA 6-series airfoil tabulated data, fits splines, and returns a
        list of x and y points with the desired number of points.
        Returns: [x, y] points.
        """
        
        self.path = path
        self.n_points = n_points
        self.profile = profile
        
        with open(path, 'r') as f:
            data = json.load(f)
        # Assume JSON has keys 'upper' and 'lower'
        upper = np.array(data[profile]['upper'])
        lower = np.array(data[profile]['lower'])

        # Fit CubicSplines
        cs_upper = CubicSpline(upper[:,0], upper[:,1])
        cs_lower = CubicSpline(lower[:,0], lower[:,1])

        # Cosine spacing for better point distribution
        def cosine_spacing(xmin, xmax, n):
            beta = np.linspace(0, np.pi, n)
            return 0.5 * (xmin + xmax) + 0.5 * (xmax - xmin) * np.cos(beta)

        n_half = n_points // 2 + 1
        x_upper = cosine_spacing(upper[:,0].min(), upper[:,0].max(), n_half)
        x_lower = cosine_spacing(lower[:,0].min(), lower[:,0].max(), n_half)

        y_upper = cs_upper(x_upper)
        y_lower = cs_lower(x_lower)
        
        # Turn to [x,y] format
        upper_points = list(zip(x_upper, y_upper))
        lower_points = list(zip(x_lower, y_lower))
        
        # XY list
        xy = upper_points + lower_points[:-1][::-1]
        self.xy = np.array(xy).tolist()
        
if __name__ == '__main__':
    
    test = 2
    
    if test == 1:
    
        # Test 1
        # work directory is the root directory /05 App
        path = './coords/NACA63430.txt'
        airfoil = Airfoil(path=path, name='NACA63430')
        path = './coords/circle.txt'
        circle = Airfoil(path=path, name='circle')
        circle.exportAirfoil()
    
    elif test == 2:
        
        # Test 2
        # Task: NACA 6 inclusion
        path = './edfoil/naca/naca_6.json'
        airfoil = Airfoil(name='NACA6')
        airfoil.naca6(path=path, profile='63-206' ,n_points=100)
        x = [x[0] for x in airfoil.xy]
        y = [x[1] for x in airfoil.xy]
        
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(10,6))
        ax.set_title('NACA 63-206 - 100 points')
        ax.plot(x,y)
        ax.axis('equal')
        plt.show()