"""
Create a graphical version of the hex map
"""

import logging

import lxml.etree as etree

from Tkinter import *

import math

def sin60(a):
    return (a * 8660) / 10000

import hexmap

class Map(hexmap.Map, Canvas):

    def __init__(self, master, 
                 size, origin=hexmap.Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None, hexrun=15):

        logger = logging.getLogger(self.__class__.__name__ + ".__init__")

        logger.debug("Origin = %s" % origin)

        hexmap.Map.__init__(self, size, origin, terrains, tokens, 
                        name, game, copyright)

        self.hexrun = hexrun
        self.porigin = hexmap.Point(self.hexradius, self.hexheight)
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
    def hexwidth(self): return self._hexwidth

    @property
    def hexrise(self): return self._hexrise

    @property
    def hexheight(self): return self._hexheight

    @property
    def canvasSize(self):
        x = (self.hexrun * 3 * self.size.hx) + self.hexrun
        y = (self.hexheight * self.size.hy) + self.hexrise
        return hexmap.Point(x, y)

    def hexcenter(self, vec):
        ybias = math.floor(vec.hx / 2)
        px = ((vec.hx * 3) * self.hexrun) + self.porigin.x
        py = (((vec.hy * 2) - vec.hx) * self.hexrise) + self.porigin.y
        return hexmap.Point(px, py)

    def hexvertices(self, vec):
        center = self.hexcenter(vec)
        xpoints = [center.x - self.hexradius, center.x - self.hexrun,
                   center.x + self.hexrun, center.x + self.hexradius]
        ypoints = [center.y - self.hexrise, center.y, center.y + self.hexrise]

        plist = [
            hexmap.Point(xpoints[1], ypoints[0]),
            hexmap.Point(xpoints[2], ypoints[0]),
            hexmap.Point(xpoints[3], ypoints[1]),
            hexmap.Point(xpoints[2], ypoints[2]),
            hexmap.Point(xpoints[1], ypoints[2]),
            hexmap.Point(xpoints[0], ypoints[1]),
            ]
        return plist

    def tokencenter(self, vec): return self.hexcenter(vec)

    def clickrange(self, vec): return self.hexradius

    def clickdistance(self, p, vec):
        center = self.hexcenter(vec)
        return len(center - point)


    def inrange(self, p, vec):
        return self.clickdistance(p, vec) < self.clickrange(vec)

    def rectangle(self, p0, offset=hexmap.Point(0, 0)):
        # Given the center point of a hex, find the vertices of the rectangle
        # which defines the boundaries
        # These rectangles fill the plane completely in the same way that the
        # hexagons do.

        v0 = hexmap.Point(p0.x - self.hexradius + offset.x, 
                          p0.y - self.hexrise + offset.y)
        v1 = hexmap.Point(v0.x, p0.y + self.hexrise + offset.y)
        v2 = hexmap.Point(p0.x + self.hexrun + offset.x, v1.y)
        v3 = hexmap.Point(v2.x, v0.y)
        #self.create_rectangle(v0.x, v0.y, v2.x, v2.y)

        vertices = (v0, v1, v2, v3)
        return vertices

    def refhex(self, p):
        # generate the base hex which contains a given point
        # offset by the porigin + 1/2 hex ( to get the origin hex on the
        # canvas
        hx = ((p.x - self.porigin.x) + self.hexradius) / (self.hexrun * 3)
        hy = ((p.y - self.porigin.y) + ((hx + 1) * self.hexrise)) / self.hexheight
        return hexmap.Vector(hx, hy)

    def point2hex(self, p):
        # Find the reference hex containing this point
        h = self.refhex(p)

        # find the center of that hex
        c = self.hexcenter(h)

        # get the bounding rectangle of the expected hex
        # offset the rectangle by -hexradius to make the slope calculation
        # simpler
        r = self.rectangle(c, offset=hexmap.Point(-self.hexradius, 0))

        # find the point inside a normalized rectangle
        # offset by hexradius to make further tests easier
        # the axis point is placed at 0,0 of the normalized rectangle containing
        # the point
        np = hexmap.Point(p.x - r[0].x - self.hexradius, p.y - r[0].y - self.hexrise)
        if np.x <= self.hexrun and np.x * 2 < abs(np.y):
            if np.y > 0:
                h += hexmap.Vector.UNIT[4]
            else:
                h += hexmap.Vector.UNIT[5]

        return h

    def canvaspoint(self, eventpoint):
        """
        Convert a click point to a canvas point, accounting for scrolling
        """

        return hexmap.Point(
            self.canvasx(eventpoint.x),
            self.canvasy(eventpoint.y)
            )


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
        
