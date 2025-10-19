'''
Serialisation and deserialisation of session data to/from .edf files.
'''

from __future__ import annotations
import json
from datetime import datetime
import numpy as np
import pandas as pd

# Load libraries
from edfoil.classes.airfoil import Airfoil
from edfoil.classes.station import Station
from edfoil.classes.section import Section
from edfoil.classes.session import session

def _to_float(x):
    
    '''
    Convert a value to float or int if possible.
    
    :param x: Value to convert.
    :type x: any
    
    :returns: Converted float or int value, or original value if conversion fails.
    :rtype: float, int, or original type
    '''
    
    try:
        if isinstance(x, (np.floating,)):
            return float(x)
        if isinstance(x, (np.integer,)):
            return int(x)
    except Exception:
        pass
    return x

def _to_list_xy(xy):
    
    '''
    Convert a list of (x,y) pairs to a list of [float, float] lists.
    
    :param xy: List of (x,y) pairs.
    :type xy: list[tuple[float,float],...] 
    
    :returns: List of [float, float] lists.
    :rtype: list[list[float,float],...]
    '''
    
    # list[(x,y),...] -> [[float,float],...]
    out = []
    for p in xy:
        x, y = p
        out.append([_to_float(x), _to_float(y)])
    return out

def serialise_airfoil(a) -> dict:
    
    '''
    Serialise an Airfoil object to a dictionary.
    
    :param a: Airfoil object to serialise.
    :type a: Airfoil
    
    :returns: Dictionary representation of the Airfoil.
    :rtype: dict
    '''
    
    # Expect attributes: name, family, profile, xy (iterable of (x,y))
    return {
        "name": getattr(a, "name", None),
        "family": getattr(a, "family", None),
        "profile": getattr(a, "profile", None),
        "xy": _to_list_xy(getattr(a, "xy", [])),
    }

def serialise_station(s) -> dict:
    
    '''
    Serialise a Station object to a dictionary.
    
    :param s: Station object to serialise.
    :type s: Station
    
    :returns: Dictionary representation of the Station.
    :rtype: dict
    '''
    
    # Store by airfoil name + parameters (primitives only)
    airfoil_name = getattr(s, "airfoil", None)
    if hasattr(airfoil_name, "name"):
        airfoil_name = airfoil_name.name
    params = dict(getattr(s, "parameters", {}))
    # Coerce numerics
    for k, v in params.items():
        if isinstance(v, (list, tuple)):
            params[k] = [_to_float(i) for i in v]
        else:
            params[k] = _to_float(v)
    return {
        "airfoil": airfoil_name,
        "parameters": params,
    }

def _df_to_records(df: pd.DataFrame | None):

    '''
    Convert a DataFrame to a list of records (dictionaries).
    Each record corresponds to a row in the DataFrame.
    
    :param df: Pandas DataFrame to convert.
    :type df: pd.DataFrame | None
    
    :returns: List of records with native Python types.
    :rtype: list[dict] | None
    '''

    if df is None:
        return None
    if not isinstance(df, pd.DataFrame):
        return None
    # Records with native Python types
    recs = []
    for rec in df.to_dict("records"):
        recs.append({k: _to_float(v) for k, v in rec.items()})
    return recs

def serialise_section(sec) -> dict:
    
    '''
    Serialise a Section object to a dictionary.
    
    :param sec: Section object to serialise.
    :type sec: Section
    
    :returns: Dictionary representation of the Section.
    :rtype: dict
    '''
    
    # Minimal: keep parameters (you can add points if needed)
    params = dict(getattr(sec, "parameters", {}))
    for k, v in params.items():
        if isinstance(v, (list, tuple)):
            params[k] = [_to_float(i) for i in v]
        else:
            params[k] = _to_float(v)
    # Optional: include a lightweight snapshot of points if desired
    # points = getattr(sec, "points", None)
    # if points: ... (convert recursively to floats)
    return {"parameters": params}

def serialise_session(db) -> dict:

    '''
    Serialise a session object to a dictionary.
    
    :param db: Current session() instance.
    :type db: session
    
    :returns: Dictionary representation of the session.
    :rtype: dict
    '''

    airfoils = {}
    for name, a in getattr(db.airfoils, "items")():
        airfoils[name] = serialise_airfoil(a)

    stations = {}
    for name, s in getattr(db.stations, "items")():
        stations[name] = serialise_station(s)

    sections = {}
    for name, sec in getattr(db, "sections", {}).items():
        sections[name] = serialise_section(sec)

    settings = dict(getattr(db, "settings", {}))

    blade = {}
    bdict = getattr(db, "blade", {})
    if isinstance(bdict, dict):
        blade["overlap"] = _df_to_records(bdict.get("overlap"))
        blade["ovp_text"] = _df_to_records(bdict.get("ovp_text"))
        blade["olp_len"] = _df_to_records(bdict.get("olp_len"))

    return {
        "version": "0.3.1",
        "saved_at": datetime.now().isoformat(timespec="seconds"),
        "airfoils": airfoils,
        "stations": stations,
        "sections": sections,
        "settings": settings,
        "blade": blade,
    }

def save_session_to_edf(db, file_path: str) -> None:
    
    '''
    Save the current session object to a .edf file.
    
    :param db: Current session() instance.
    :type db: session
    
    :param file_path: Path to save the .edf file.
    :type file_path: str
    
    :returns: None.
    :rtype: None
    '''
    
    payload = serialise_session(db)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
# Load Functions
def _list_of_pairs_to_tuples(lst):
    
    '''
    Convert a list of [x, y] lists to a list of (float, float) tuples.
    
    :param lst: List of [x, y] lists.
    :type lst: list[list[float, float], ...]
    
    :returns: List of (float, float) tuples.
    :rtype: list[tuple[float, float], ...]
    '''
    
    return [(float(x), float(y)) for x, y in lst or []]

def load_session_from_edf(file_path: str) -> session:
    
    '''
    Load a session object from a .edf file.
    
    :param file_path: Path to the .edf file.
    :type file_path: str
    
    :returns: Loaded session() instance.
    :rtype: session
    '''
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = session()

    # ---- Airfoils ----
    for name, a in (data.get("airfoils") or {}).items():
        try:
            af = Airfoil()
            # assign basic fields
            af.name = a.get("name", name)
            af.family = a.get("family", "")
            af.profile = a.get("profile", "")
            af.update(a.get("xy", []))
            db.airfoils.add(af.name, af)
            print(f'Loaded airfoil: {af.name} with {len(af.xy)} points')
        except Exception:
            # fallback minimal
            af = Airfoil()
            af.name = name
            af.xy = []
            db.airfoils.add(af.name, af)
            print(f'Failed to load airfoil: {name}. Created empty placeholder.')

    # ---- Stations ----
    for name, s in (data.get("stations") or {}).items():
        a_name = s.get("airfoil")
        airfoil_obj = db.airfoils.get(a_name, None)
        if airfoil_obj is None:
            # skip station if airfoil missing
            continue
        p = s.get("parameters") or {}
        station = Station(
            airfoil=airfoil_obj,
            chord=float(p.get("chord", 1.0)),
            twist_angle=float(p.get("twist_angle", 0.0)),   # already in radians
            x_offset=float((p.get("offset") or [0,0,0])[0]),
            y_offset=float((p.get("offset") or [0,0,0])[1]),
            z_offset=float((p.get("offset") or [0,0,0])[2]),
            x_multiplier=float((p.get("multiplier") or [1,1,1])[0]),
            y_multiplier=float((p.get("multiplier") or [1,1,1])[1]),
            z_multiplier=float((p.get("multiplier") or [1,1,1])[2]),
            x_mirror=bool((p.get("mirror") or [False, True])[0]),
            y_mirror=bool((p.get("mirror") or [False, True])[1]),
        )
        db.stations.add(name, station)

    # ---- Sections (rebuild from parameters) ----
    for name, sec in (data.get("sections") or {}).items():
        p = sec.get("parameters") or {}
        # link to correct station
        z = float(p.get("z", 0.0))
        sta_key = f"sta_{int(z)}"
        station_obj = db.stations.get(sta_key)
        if station_obj is None:
            # skip if station not present
            continue
        section = Section(
            station=station_obj,
            n_plies=int(p.get("n_plies", 1)),
            ply_thickness=float(p.get("ply_thickness", 1.0)),
            overlap_target=float(p.get("overlap_target", 10.0)),
            te_thickness=float(p.get("te_thickness", 1.0)),
            bond_thickness=float(p.get("bond_thickness", 1.0)),
            saveFig=bool(p.get("saveFig", False)),
            tolerance=int(p.get("tolerance", 6)),
            ini_u0=float(p.get("ini_u0", p.get("u0_initial", 21.0))),
        )
        db.sections[name] = section

    # ---- Settings ----
    db.settings.update(data.get("settings") or {})

    # ---- Blade (rebuild DataFrames) ----
    blade = data.get("blade") or {}
    if "overlap" in blade and isinstance(blade["overlap"], list):
        db.blade["overlap"] = pd.DataFrame(blade["overlap"])
    if "ovp_text" in blade and isinstance(blade["ovp_text"], list):
        db.blade["ovp_text"] = pd.DataFrame(blade["ovp_text"])
    if "olp_len" in blade and isinstance(blade["olp_len"], list):
        db.blade["olp_len"] = pd.DataFrame(blade["olp_len"])

    return db