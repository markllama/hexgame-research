"""
the HexMap represents a game map made up of a set of hexagons
"""

import math
import numbers

#import xml.etree.ElementTree as etree
import lxml.etree as etree

class Vector(object):
    """
    A single location in a hexagonal lattice.  This class allows
    calculation with hex locations
    """
    
    def __init__(self, *args, **kargs):
        """
        Vector()  - generate a 

        signatures:

          int hx, int hy
          Vector hv

        """
        self._hx = None
        self._hy = None

        if len(args) == 0 and len(kargs) == 0:
            self._hx = 0
            self._hy = 0

        if len(args) == 1:
            hv = args[0]
            if isinstance(hv, Vector):
                hv = args[0]
                (self._hx, self._hy) = (hv.hx, hv.hy)
            else:
                raise HexMapException("hv is not a Vector")
        
        elif len(args) == 2:
            # check if they're integers
            (self._hx, self._hy) = (args[0], args[1])

        elif "hx" in kargs and "hy" in kargs:
            (self._hx, self._hy) = (kargs['hx'], kargs['hy'])

        elif "hv" in kargs:
            (self._hx, self._hy) = (kargs['hv'].hx, kargs['hv'].hy)

        if self._hx is None:
            raise AttributeException("unable to determine hx or hy")

    @property
    def hx(self): return self._hx

    @property
    def hy(self): return self._hy
    
    @property
    def hz(self): return self._hy - self._hx

    @staticmethod
    def fromelement(element):
        """
        create an object from an XML element
        """
        
        # Check that it's an Element and that it's tag is "vector"
        return Vector(hx=int(element.get('hx')), hy=int(element.get('hy')))
        
    @staticmethod
    def fromxml(xmlstring):
        """
        create an object from an XML string
        """
        return Vector.fromelement(etree.fromstring(xmlstring))


    def __repr__(self):
        return self.__class__ + "(hx=%d, hy=%d)" % (self.hx, self.hy)

    #def __str__(self):
    #    return 

    @property
    def element(self):
        e = etree.Element("vector")
        e.set('hx', str(self.hx))
        e.set('hy', str(self.hy))
        return e
        
    @property
    def xml(self):
        return '<vector hx="%d" hy="%d" />' % (self.hx, self.hy)


    #
    # Math functions
    #
    def __len__(self):
        return max( self.hx, self.hy, self.hz)

    def __eq__(self, other):
        assert(isinstance(other, Vector))
        
    def __add__(self, other):
        assert(isinstance(other, Vector))
        return Vector(self.hx + other.hx, self.hy + other.hy)

    def __sub__(self, other):
        assert(isinstance(other, Vector))
        return Vector(other.hx - self.hx, other.hy - self.hy)

    def distance(self, other):
        assert(isinstance(other, Vector))
        return len(other - self)

    @property
    def hextant(self):
        ux, uy, uz  = 0, 0, 0

        # get non normalized non-zero components
        if self.hx != 0: ux = self.hx / abs(self.hx)
        if self.hy != 0: uy = self.hy / abs(self.hy)
        if self.hz != 0: uz = self.hz / abs(self.hz)
        
        # Create a normalized vector
        hunit = Vector(ux, uy)
        for i in range(0, 6):
            if hunit == UNIT[i] and hunit.hz == uz:
                return i

        for i in range(0, 6):
            c = HEXTANT[i]
            if ux == c[0] and uy == c[1] and uz == c[2]:
                return i

        raise VectorError("no hextant")

    def rotate(self, hextants=1):
        a = (self.hy, self.hx, -self.hz, -self.hy, -self.hx, self.hz, self.hy)
        r = hextants % 6
        return Vector(a[r+1], a[r])

    @property
    def bearing(self):
        h = self.hextant
        n = self.rotate(-h)
        f = abs(n.hx) / len(this)
    
        return h + f

    def angle(self, other):
        b = self.bearing
        o = other.bearing

        # normalize o
        if o < b: o += 6
        return o - b

ORIGIN = Vector()

UNIT = (
    Vector(0, -1),
    Vector(1, 0),
    Vector(1, 1),
    Vector(0, 1),
    Vector(-1, 0),
    Vector(-1, -1)
    )

HEXTANT = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    ( 1,  1,  1),
    (-1,  1,  1),
    (-1, -1,  1),
    (-1, -1, -1)
    )
