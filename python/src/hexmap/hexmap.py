"""
"""
import lxml.etree as etree

from vector import Vector

class HexMap(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin=Vector.ORIGIN, terrains={}, tokens={}):

        # name
        # game
        # copyright

        self._size = size
        self._origin = origin

        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains
        self._tokens = tokens

    # a factory from an XML map
    @staticmethod
    def fromelement(eroot):
        pass

    @staticmethod
    def fromstring(mapstring):
        pass

    @property
    def element(self):
        pass

    @property
    def xml(self):
        pass

    @property
    def size(self):
        return self._size

    @property
    def origin(self):
        return self._origin

