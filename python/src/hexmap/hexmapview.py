"""
Create a graphical version of the hex map
"""

import logging

import lxml.etree as etree

from Tkinter import *

import math

def sin60(a):
    return (a * 8660) / 10000

from hexmap import HexMap
from vector import Vector
from point import Point
from terrain import Terrain

class HexMapView(HexMap, Frame):

    def __init__(self, size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None, hexrun=15):

        logger = logging.getLogger(self.__class__.__name__ + ".__init__")

        logger.debug("Origin = %s" % origin)

        HexMap.__init__(self, size, origin, terrains, tokens, 
                        name, game, copyright)

        self.hexrun = hexrun
        self.porigin = Point(self.hexradius, self.hexheight)
        self.porigin = self.hexcenter(self.origin)

        # create a frame
        Frame.__init__(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(self)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        # bind the scroll bars to the canvas
        canvassize = self.canvasSize

        canvas = Canvas(self, bd=0,
                        width=canvassize.x, height=canvassize.y,
                        scrollregion = (0, 0, canvassize.x, canvassize.y),
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set)

        canvas.grid(row=0, column=0, sticky=N+S+E+W)

        xscrollbar.config(command=canvas.xview)
        yscrollbar.config(command=canvas.yview)

        # install two scroll bars


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

    def hexcenter(self, vec):
        ybias = math.floor(vec.hx / 2)
        px = ((vec.hx * 3) * self.hexrun) + self.porigin.x
        py = (((vec.hy * 2) - vec.hx) * self.hexrise) + self.porigin.y
        return Point(px, py)

    def tokencenter(self, vec): return self.hexcenter(vec)

    def clickrange(self, vec): return self.hexradius

    def clickdistance(self, p, vec):
        center = self.hexcenter(vec)
        return len(center - point)


    def inrange(self, p, vec):
        return self.clickdistance(p, vec) < self.clickrange(vec)

    def refloc(self, p):
        hx = math.floor((p.x, self.porigin.x) / self.hexrun + 3)
        hy = math.floor(
            ((p.y - self.porigin.y) + (hx * self.hexrise))
            / self.hexheight)

    def refbox(self, p):
        refloc = self.refloc(p)
        return [refloc,refloc + Vector.UNIT[2], refloc + Vector.UNIT[3]]

    def point2vector(self, p):
        triangle = self.refbox(p)
        m = self
        bydist = lambda a, b: m.clickdistance(p, a) - m.clickdistance(p, b)
        triangle.sort(bydist)
        return triangle[0]

    def canvaspoint(self, eventpoint):
        """
        Convert a click point to a canvas point.  This is based on
        Javascript click behavior
        """
        canvascorner = Point(0, 0)
        scrollcorner = Point(0, 0)
        return (eventpoint - canvascorner) + scrollcorner

    def redraw(self):
        pass


class TerrainView(Terrain):
    """
    A Terrain that knows how to draw itself when it's added to map
    """

    @property
    def map(self): return self._map

    # map property is inherited from Terrain
    @map.setter
    def map(self, map):
        """
        Draw itself on each location
        """
        print "adding a map to me: map = %s, I am %s" % (map, self.name)
