#
# A location on a hex map
#

#class Vector():

#    def __init__(self, hx=0, hy=0):
#        self.hx = hx
#        self.hy = hy

#    def __composite_values__(self):
#        return self.hx, self.hy

#    def __repr__(self):
#        return "Vector(hx=%d, hy=%d)" % (self.hx, self.hy)

#    def __eq__(self, other):
#        return isinstance(other, Vector) and \
#            other.hx == self.hx and \
#            other.hy == self.hy

#    def __ne__(self, other):
#        return not self.__eq__(other)

"""
the HexMap represents a game map made up of a set of hexagons
"""

import math
import numbers

#import xml.etree.ElementTree as etree
import lxml.etree as etree

class Vector():
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

    def __composite_values__(self):
        return self.hx, self.hy

    def copy(self):
        return Vector(self)

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
        return self.__class__.__name__ + "(hx=%d, hy=%d)" % (self.hx, self.hy)

#    def __str__(self):
#        return repr(self)

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
        return max( abs(self.hx), abs(self.hy), abs(self.hz))

    def __eq__(self, other):
        assert(isinstance(other, Vector))
        return self.hx == other.hx and self.hy == other.hy
        
    def __add__(self, other):
        assert(isinstance(other, Vector))
        return self.__class__(self.hx + other.hx, self.hy + other.hy)

    def __sub__(self, other):
        assert(isinstance(other, Vector))
        return self.__class__(self.hx - other.hx, self.hy - other.hy)

    def __mul__(self, scalar):
        return self.__class__(self.hx * scalar, self.hy * scalar)

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
            if hunit == Vector.UNIT[i] and hunit.hz == uz:
                return i

        for i in range(0, 6):
            c = Vector.HEXTANT[i]
            if ux == c[0] and uy == c[1] and uz == c[2]:
                return i

        raise VectorError("no hextant")

    def rotate(self, hextants=1):
        a = (self.hy, self.hx, -self.hz, -self.hy, -self.hx, self.hz, self.hy)
        r = hextants % 6
        return Vector(a[r+1], a[r])

    @property
    def bearing(self):
        # determine the vector's hextant
        h = self.hextant

        # rotate the vector back to the x axis
        n = self.rotate(-h)

        f = float(abs(n.hx)) / len(self)
    
        return h + f

    def angle(self, other):
        b = self.bearing
        o = other.bearing

        # normalize o
        if o < b: o += 6
        return o - b

    @property
    def neighbors(self):
        return [self + offset for offset in Vector.UNIT]

Vector.ORIGIN = Vector()

Vector.UNIT = (
    Vector(0, -1),
    Vector(1, 0),
    Vector(1, 1),
    Vector(0, 1),
    Vector(-1, 0),
    Vector(-1, -1)
    )

Vector.HEXTANT = (
    ( 1, -1, -1),
    ( 1,  1, -1),
    ( 1,  1,  1),
    (-1,  1,  1),
    (-1, -1,  1),
    (-1, -1, -1)
    )
