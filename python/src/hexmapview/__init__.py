"""
Extend the hexmap module to allow local drawing.
"""

# These three classes are not extended.
from hexmap import Point, Vector, AllHexes

# These are extended from hexmap
from map import Map
from terrain import Terrain
# from token import Token
from hexmap import Hex

# these are new, used to help draw the map
from centerterrain import CenterTerrain
from borderterrain import BorderTerrain
