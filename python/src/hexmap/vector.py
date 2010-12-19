"""
the HexMap represents a game map made up of a set of hexagons
"""

import math
import numbers

import xml.etree.ElementTree as etree

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

    
