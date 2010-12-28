"""
Create a graphical version of the hex map
"""

from Tkinter import *

def sin60(a):
    return (a * 8660) / 10000

from hexmap import HexMap
from vector import Vector


class HexMapView(HexMap):

    def __init__(self, size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None, hexrun=15):


        HexMap.__init__(self, size, origin, terrains, tokens, 
                        name, game, copyright)

        # setting this syncs the others
        self.hexrun = hexrun

    # All of the hex dimensions are based off the hexrun
    @property
    def hexrun(self): return self._hexrun

    @hexrun.setter
    def hexrun(self, value):
        self._hexrun = value
        self._hexradius = value * 2
        self._hexwidth = value * 4
        self._hexrise = sin60(self._hexradius)
        self._hexheight = self._hexrise * 2

    @property
    def hexradius(self): return self._hexradius
        
    @property
    def hexrise(self): return self._hexrise

    @property
    def hexheight(self): return self._hexheight

    @property
    def canvasSize(self):
        x = (self.hexrun * 3 * self.size.hx) + self.hexrun
        y = (self.hexheight * self.size.hy) + self.hexrise
        return Point(x, y)
