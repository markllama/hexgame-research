"""
Create a graphical version of the hex map
"""

from hexmap import HexMap
from vector import Vector

from Tkinter import *

class HexMapView(HexMap):

    def __init__(self, size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None, hexrun=15):


        HexMap.__init__(self, size, origin, terrains, tokens, 
                        name, game, copyright, hexruns)
