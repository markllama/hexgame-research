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

class HexMapView(HexMap, Canvas):

    def __init__(self, master, 
                 size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None, hexrun=15):

        logger = logging.getLogger(self.__class__.__name__ + ".__init__")

        logger.debug("Origin = %s" % origin)

        HexMap.__init__(self, size, origin, terrains, tokens, 
                        name, game, copyright)

        self.hexrun = hexrun
        self.porigin = Point(self.hexradius, self.hexheight)
        self.porigin = self.hexcenter(self.origin)

        # bind the scroll bars to the canvas
        canvassize = self.canvasSize

        Canvas.__init__(self, master, bd=0,
                        width=canvassize.x, height=canvassize.y,
                        scrollregion = (0, 0, canvassize.x, canvassize.y),
                        )


        # install two scroll bars

        #self.repaint()

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

    def hexvertices(self, vec):
        center = self.hexcenter(vec)
        xpoints = [center.x - self.hexradius, center.x - self.hexrun,
                   center.x + self.hexrun, center.x + self.hexradius]
        ypoints = [center.y - self.hexrise, center.y, center.y + self.hexrise]

        plist = [
            Point(xpoints[1], ypoints[0]),
            Point(xpoints[2], ypoints[0]),
            Point(xpoints[3], ypoints[1]),
            Point(xpoints[2], ypoints[2]),
            Point(xpoints[1], ypoints[2]),
            Point(xpoints[0], ypoints[1]),
            ]
        return plist

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

    def repaint(self):
        logger = logging.getLogger(self.__class__.__name__ + ".repaint")
        logger.debug("Repainting map")

        # remove all existing objects?

        # draw all of the terrains
        logger.debug("there are %d terrains" % len(self._terrains))
        for terrain in self._terrains:
            terrain.repaint()

        # draw all of the tokens
        for token in self._tokens:
            token.repaint()
        
class TerrainView(Terrain):
    """
    A Terrain that knows how to draw itself when it's added to map
    """

#    @property
#    def map(self): return self._map

#    # map property is inherited from Terrain
#    @map.setter
#    def map(self, map):
#        """
#        Draw itself on each location
#        """
#        print "adding a map to me: map = %s, I am %s" % (map, self.name)

class BorderTerrainView(TerrainView):
    """Draw the hex shape around the center"""

    def repaint(self):
        """Draw the border around the hex's location(s)"""
        logger = logging.getLogger(self.__class__.__name__ + ".repaint")


        for l in self.locations:
            center = self._map.hexcenter(l)
            vertices = self._map.hexvertices(l)
            coordinates = []
            for v in vertices: coordinates.extend([v.x, v.y]) 
            self._map.create_polygon(
                coordinates, 
                fill="white", 
                outline="black", 
                tag=["border", "(%d,%d)" % (l.hx, l.hy)]
                )
