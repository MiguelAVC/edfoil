import numpy as np
import os
import matplotlib.pyplot as plt
from edfoil.classes.airfoil import Airfoil

class Station:
    def __init__(
        self,
        airfoil: Airfoil, 
        chord : float,
        twist_angle : float,
        x_offset : float = 0.0,
        y_offset : float = 0.0,
        z_offset : float = 0.0,
        x_multiplier : float = 1.0,
        y_multiplier : float = 1.0,
        z_multiplier : float = 1.0,
        x_mirror : bool = False,
        y_mirror : bool = True,
        path : str = None, # Deprecated
    ) -> None:
        
        """Station class.

        Args:
            chord (float): Chord length.
            twist_angle (float): Twist angle in degrees.
            x_offset (float, optional): x offset from origin. Defaults to 0.0.
            y_offset (float, optional): y offset from origin. Defaults to 0.0.
            z_offset (float, optional): z offset from origin. Defaults to 0.0.
            x_multiplier (float, optional): x coordinate multiplier, increases
            length of airfoil. Defaults to 1.0.
            y_multiplier (float, optional): y coordinate multiplier, increases
            airfoil. Defaults to 1.0.
            z_multiplier (float, optional): z coordinate multiplier, increases
            station distance. Defaults to 1.0.
            x_mirror (bool, optional): To flip airfoil in the y axis. 
            Defaults to False.
            y_mirror (bool, optional): To flip airfoil in the x axis. 
            Defaults to True.
            path (str, optional): Full path to the .txt file containing airfoil
            data [Deprecated].
        """
        
        # Setting parameters
        self.parameters ={
            'chord':chord,
            'twist_angle':np.radians(twist_angle),
            'offset':(x_offset,y_offset,z_offset),
            'multiplier':(x_multiplier,y_multiplier,z_multiplier),
            'mirror':(x_mirror,y_mirror),
        }
        
        twist_angle_rad = np.radians(twist_angle)
        # DEPRECATED
        # coordinates = np.genfromtxt(path)
        # self.airfoil = path.split('\\')[-1][:-4]
        coordinates = np.array(airfoil.xy)
        self.airfoil = airfoil.name
        
        # Define if it is a circle
        tolerance:float = 1e-1
        centre = np.mean(coordinates, axis=0)
        distance_to_centre = np.linalg.norm(coordinates-centre,axis=1)
        radius = np.mean(distance_to_centre)
        self.parameters['isCircle'] = bool(np.all(np.abs(distance_to_centre - radius) < tolerance))
        
        # Generating station
        x_original = coordinates[:,0]
        y_original = coordinates[:,1]
        
        # Scaling
        if x_mirror == True:
            x_mirror = -1
        else:
            x_mirror = 1
            
        if y_mirror == True:
            y_mirror = -1
        else:
            y_mirror = 1
        
        x_scaled = x_original * chord * x_multiplier * x_mirror
        y_scaled = y_original * chord * y_multiplier * y_mirror

        # Rotating
        xy_rotated = np.column_stack((x_scaled,y_scaled))

        rotation_matrix = [
            [np.cos(twist_angle_rad), -np.sin(twist_angle_rad)],
            [np.sin(twist_angle_rad), np.cos(twist_angle_rad)]
        ]

        xy_rotated = np.dot(xy_rotated,rotation_matrix)

        # Offsetting
        x_offset = xy_rotated[:,0] + x_offset
        y_offset = xy_rotated[:,1] + y_offset

        coordinates_station = np.column_stack((x_offset,y_offset))
        
        self.xy = coordinates_station
        
    def plot(self, name) -> None:
        fig, ax = plt.subplots(figsize=(10,6))

        x = self.xy[:,0]
        y = self.xy[:,1]

        ax.plot(x, y)

        ax.set_xlabel('x [-]')
        ax.set_ylabel('y [-]')
        ax.minorticks_on()
        ax.tick_params(axis='both', which='both', direction='in', top=True,
                    right = True, labelsize='large')
        ax.set_title(f'{self.airfoil} - {name}')
        ax.grid(which='major')
        ax.axis('equal')

        plt.tight_layout()
        plt.show()
        
    def xyRange(self) -> list[list[float]]:
        range_list = [
            [float(np.min(self.xy[:,col])),float(np.max(self.xy[:,col]))] 
            for col in range(2)
        ]
        return range_list

# %% Debugging

if __name__ == '__main__':
    
    test = 2
    
    # Test 1
    
    if test == 1:
        sta = Station(
            path=os.path.join(os.getcwd(),'edfoil','airfoils','NACA63416.txt'),
            chord=1334,
            twist_angle=24.3,
            x_offset=-474.26,
            y_offset=255,
            z_offset=1500,
            y_multiplier=1.55,
            y_mirror=True,
        )
        
        sta.plot('Final')
        print(sta.parameters['isCircle'])
    
    # Test 2
    # Task: Airfoil implementation and path deprecation
    
    elif test == 2:
        
        path = 'edfoil/airfoils/NACA63416.txt'
        # path = 'edfoil/airfoils/circle.txt'
        airfoil = Airfoil(name='example')
        airfoil.importCoords(path=path)
        
        sta = Station(
            airfoil=airfoil,
            chord=1334,
            twist_angle=24.3,
            x_offset=-474.26,
            y_offset=255,
            z_offset=1500,
            y_multiplier=1.55,
            y_mirror=True,
        )
        
        sta.plot('Final')
        print(sta.parameters['isCircle'])