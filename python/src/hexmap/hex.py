"""
This a kind of "virtual" object.  It allows access to the contents of each
hex of the map without having to duplicate objects and maintain all of the
references.  Instead, each of the attributes and properties is dynamically
determined from the contents of the map.

A Hex is meaningless when disconnected from a map.

The contents are determined entirely by the tuple (map, location)

A hex cannot change map or location after it is created.
"""

from vector import Vector

class Hex(Vector):

    def __init__(self, hx=0, hy=0, map=None):

        Vector.__init__(hx, hy)
        # check that map is hexmap.Map or None
        self._map = map

    @property
    def map(self):
        return self._map

    @property
    def terrains(self):
        if self.map is None:
            raise LookupError("No map set")

        # search all the terrains for membership in this hex
        return []

    @property
    def tokens(self):
        if self.map is None:
            raise LookupError("No map set")

        # search all the terrains for membership in this hex
        return []

    # Arithmetic operations allow you to find a related hex
    # Where a Vector would return the corresponding Vector result,
    # a Hex will return the Hex result

    def __add__(self, other):
        newloc = Vector.__add__(self, other)
        if not self.map contains newloc:
            raise KeyError
        return self.__class__(newloc.hx, newloc.hy, self.map)

    def __sub__(self, other):
        newloc = Vector.__sub__(self, other)
        if not self.map contains newloc:
            raise KeyError
        return self.__class__(newloc.hx, newloc.hy, self.map)

    def __mul__(self, other):
        newloc = Vector.__add__(self, other)
        if not self.map contains newloc:
            raise KeyError
        return self.__class__(newloc.hx, newloc.hy, self.map)
