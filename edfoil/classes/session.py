'''
Class for managing session data including airfoils and stations.

This is the main database class that holds airfoils, stations, sections, skin, blade parameters, and settings for a session in the software instance.
'''


from PySide6.QtCore import QObject, Signal

# Main database in every session.       
class session(QObject):
    
    '''
    QObject class for managing session data including airfoils and stations.
    
    :ivar airfoils: AirfoilDB instance containing airfoils in the session.
    :vartype airfoils: AirfoilDB
    
    :ivar stations: StationDB instance containing stations in the session.
    :vartype stations: StationDB
    
    :ivar sections: Dictionary containing sections in the session.
    :vartype sections: dict
    
    :ivar skin: Dictionary containing skin data in the session.
    :vartype skin: dict
    
    :ivar blade: Dictionary containing blade parameters in the session.
    :vartype blade: dict
    
    :ivar settings: Dictionary containing session settings.
    :vartype settings: dict
    
    :returns: session instance.
    :rtype: session
    '''
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.airfoils = AirfoilDB(self)
        self.stations = StationDB(self)
        self.sections = {} #TODO: SectionDB
        self.skin = {}
        self.blade = {} #TODO: Blade parameters object
        self.settings = {}
    
    # def cleanStations(self):
    #     self.stations.clear()

# QObject for emitting signals
class AirfoilDB(QObject):
    
    '''
    QObject class for managing airfoils in the session.
    
    :ivar airfoils: Dictionary containing airfoils in the session.
    :vartype airfoils: dict
    
    :returns: AirfoilDB instance.
    :rtype: AirfoilDB
    '''
    
    
    airfoilsChanged = Signal(object)    # whole dict changed
    airfoilAdded    = Signal(str)          # key
    airfoilRemoved  = Signal(str)        # key
    airfoilUpdated  = Signal(str)        # key
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._airfoils: dict[str,object] = {}  # {name: Airfoil}
    
    def all(self):
        return dict(self._airfoils)

    def keys(self):
        return list(self._airfoils.keys())

    def add(self, name:str, airfoil: object):
        self._airfoils[name] = airfoil
        self.airfoilAdded.emit(name)
        self.airfoilsChanged.emit(self._airfoils.copy())

    def remove(self, name:str):
        if name in self._airfoils:
            del self._airfoils[name]
            self.airfoilRemoved.emit(name)
            self.airfoilsChanged.emit(self._airfoils.copy())

    def update(self, name:str, airfoil:object):
        self._airfoils[name] = airfoil
        self.airfoilUpdated.emit(name)
        self.airfoilsChanged.emit(self._airfoils.copy())
        
    def values(self):
        return self._airfoils.values()

    def items(self):
        return self._airfoils.items()

    def get(self, key, default=None):
        return self._airfoils.get(key, default)

    def __contains__(self, key):
        return key in self._airfoils

    def __len__(self):
        return len(self._airfoils)

    def __iter__(self):
        return iter(self._airfoils)

    def __getitem__(self, key):
        return self._airfoils[key]

class StationDB(QObject):
    
    '''
    QObject class for managing stations in the session.
    
    :ivar stations: Dictionary containing stations in the session.
    :vartype stations: dict
    '''
    
    stationsChanged = Signal(object)     # whole dict changed
    stationAdded    = Signal(str)        # key
    stationRemoved  = Signal(str)        # key
    stationUpdated  = Signal(str)        # key
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._stations: dict[str,object] = {}  # {name: Station}
    
    def all(self):
        return dict(self._stations)

    def keys(self):
        return list(self._stations.keys())

    def add(self, name:str, station: object):
        self._stations[name] = station
        self.stationAdded.emit(name)
        self.stationsChanged.emit(self._stations.copy())

    def remove(self, name:str):
        if name in self._stations:
            del self._stations[name]
            self.stationRemoved.emit(name)
            self.stationsChanged.emit(self._stations.copy())

    def update(self, name:str, station:object):
        self._stations[name] = station
        self.stationUpdated.emit(name)
        self.stationsChanged.emit(self._stations.copy())
        
    def values(self):
        return self._stations.values()

    def items(self):
        return self._stations.items()

    def get(self, key, default=None):
        return self._stations.get(key, default)
    
    def clear(self, emit_individual: bool = False):
        if not self._stations:
            return
        
        names = list(self._stations.keys())
        self._stations.clear()

        if emit_individual:
            for name in names:
                self.stationRemoved.emit(name)

        self.stationsChanged.emit({})

    def __contains__(self, key):
        return key in self._stations

    def __len__(self):
        return len(self._stations)

    def __iter__(self):
        return iter(self._stations)

    def __getitem__(self, key):
        return self._stations[key]