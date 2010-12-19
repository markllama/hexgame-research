"""
the HexMap represents a game map made up of a set of hexagons
"""

import math
import numbers

import xml.etree.ElementTree as etree

class HexMapException(Exception): pass

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
    
        if len(args) == 1:
            hv = args[0]
            if isinstance(Vector, hv):
                hv = args[0]
                (self._hx, self._hy) = (hv.hx, hv.hy)

            raise HexMapException("hv is not a Vector")
        
        elif len(args) == 2:
            # check if they're integers
            (self._hx, self._hy) = args

        elif "hx" in kargs and "hy" in kargs:
            (self._hx, self._hy) = (kargs['hx'], kargs['hy'])

        elif "hv" in kargs:
            (self._hx, self._hy) = (kargs['hv'].hx, kargs['hv'].hy)

    @property
    def hx(self): return self._hx

    @property
    def hy(self): return self._hy
    
    @property
    def hz(self): return self._hy - self._hx


    def fromelement(element):
        """
        create an object from an XML element
        """
        
        # Check that it's an Element and that it's tag is "vector"
        return Vector(hx=element['hx'], hy=element['hy'])
        

    def fromxml(xmlstring):
        """
        create an object from an XML string
        """
        return Vector.fromelement(etree.fromstring(xmlstring))

    
class HexMap(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin, terrains={}, tokens={}):

        self._size = size
        self._origin = origin

        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains
        self._tokens = tokens

    # a factory from an XML map
    def fromelement(eroot):
        pass

    def fromstring(mapstring):
        pass


    
class Hex(object):
    """
    """
    pass

class Terrain(object):
    pass

class Token(object):
    pass
