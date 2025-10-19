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
    
    :ivar airfoilsChanged: Signal emitted when the airfoils dictionary changes.
    :vartype airfoilsChanged: Signal(object)
    
    :ivar airfoilAdded: Signal emitted when an airfoil is added.
    :vartype airfoilAdded: Signal(str)
    
    :ivar airfoilRemoved: Signal emitted when an airfoil is removed.
    :vartype airfoilRemoved: Signal(str)
    
    :ivar airfoilUpdated: Signal emitted when an airfoil is updated.
    :vartype airfoilUpdated: Signal(str)
    
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
        '''
        Returns a copy of all airfoils in the database.
        
        :returns: Dictionary of all airfoils.
        :rtype: dict
        '''
        return dict(self._airfoils)

    def keys(self):
        '''
        Returns a list of all airfoil names in the database.
        
        :returns: List of airfoil names.
        :rtype: list
        '''
        return list(self._airfoils.keys())

    def add(self, name:str, airfoil: object):
        '''
        Adds a new airfoil to the database.
        
        :param name: Name of the airfoil.
        :type name: str
        :param airfoil: Airfoil object to add.
        :type airfoil: object
        '''
        self._airfoils[name] = airfoil
        self.airfoilAdded.emit(name)
        self.airfoilsChanged.emit(self._airfoils.copy())

    def remove(self, name:str):
        '''
        Removes an airfoil from the database.
        
        :param name: Name of the airfoil to remove.
        :type name: str
        '''
        if name in self._airfoils:
            del self._airfoils[name]
            self.airfoilRemoved.emit(name)
            self.airfoilsChanged.emit(self._airfoils.copy())

    def update(self, name:str, airfoil:object):
        '''
        Updates an existing airfoil in the database.
        
        :param name: Name of the airfoil to update.
        :type name: str
        :param airfoil: Updated airfoil object.
        :type airfoil: object
        '''
        self._airfoils[name] = airfoil
        self.airfoilUpdated.emit(name)
        self.airfoilsChanged.emit(self._airfoils.copy())
        
    def values(self):
        '''
        Returns a view of all airfoil objects in the database.
        
        :returns: View of all airfoil objects.
        :rtype: dict_values
        '''
        return self._airfoils.values()

    def items(self):
        '''
        Returns a view of all airfoil items (name, object) in the database.
        
        :returns: View of all airfoil items.
        :rtype: dict_items
        '''
        return self._airfoils.items()

    def get(self, key, default=None):
        '''
        Returns the airfoil with the given key.
        
        :param key: Name of the airfoil to retrieve.
        :type key: str
        :param default: Default value to return if the airfoil is not found.
        :type default: object
        :returns: The airfoil object or the default value.
        :rtype: object
        '''
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
    
    :ivar stationsChanged: Signal emitted when the stations dictionary changes.
    :vartype stationsChanged: Signal(object)
    
    :ivar stationAdded: Signal emitted when a station is added.
    :vartype stationAdded: Signal(str)
    
    :ivar stationRemoved: Signal emitted when a station is removed.
    :vartype stationRemoved: Signal(str)
    
    :ivar stationUpdated: Signal emitted when a station is updated.
    :vartype stationUpdated: Signal(str)
    '''
    
    stationsChanged = Signal(object)     # whole dict changed
    stationAdded    = Signal(str)        # key
    stationRemoved  = Signal(str)        # key
    stationUpdated  = Signal(str)        # key
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._stations: dict[str,object] = {}  # {name: Station}
    
    def all(self):
        '''
        Returns a copy of all stations in the database.
        
        :returns: Dictionary of all stations.
        :rtype: dict
        '''
        return dict(self._stations)

    def keys(self):
        '''
        Returns a list of all station names in the database.
        
        :returns: List of station names.
        :rtype: list
        '''
        return list(self._stations.keys())

    def add(self, name:str, station: object):
        '''
        Adds a new station to the database.
        
        :param name: Name of the station.
        :type name: str
        :param station: Station object to add.
        :type station: object
        '''
        self._stations[name] = station
        self.stationAdded.emit(name)
        self.stationsChanged.emit(self._stations.copy())

    def remove(self, name:str):
        '''
        Removes a station from the database.
        
        :param name: Name of the station to remove.
        :type name: str
        '''
        if name in self._stations:
            del self._stations[name]
            self.stationRemoved.emit(name)
            self.stationsChanged.emit(self._stations.copy())

    def update(self, name:str, station:object):
        '''
        Updates an existing station in the database.
        
        :param name: Name of the station to update.
        :type name: str
        :param station: Updated station object.
        :type station: object
        '''
        self._stations[name] = station
        self.stationUpdated.emit(name)
        self.stationsChanged.emit(self._stations.copy())
        
    def values(self):
        '''
        Returns a view of all station objects in the database.
        
        :returns: View of station objects.
        :rtype: dict_values
        '''
        return self._stations.values()

    def items(self):
        '''
        Returns a view of all station name-object pairs in the database.
        
        :returns: View of station name-object pairs.
        :rtype: dict_items
        '''
        return self._stations.items()

    def get(self, key, default=None):
        '''
        Retrieves a station from the database.
        
        :param key: Name of the station to retrieve.
        :type key: str
        :param default: Default value if station not found.
        :type default: object, optional
        :returns: Station object or default value.
        :rtype: object
        '''
        return self._stations.get(key, default)
    
    def clear(self, emit_individual: bool = False):
        '''
        Clears all stations from the database.
        
        :param emit_individual: Whether to emit individual removal signals for each station.
        :type emit_individual: bool
        '''
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