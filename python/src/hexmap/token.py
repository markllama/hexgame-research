"""
A single token on a hex board
"""

import lxml.etree as etree

from vector import Vector

class Token(object):
    
    def __init__(self, name, location=None, map=None):

        self._name = name
        self._location = location
        self._map = map

    @property
    def name(self): return self._name

    @property
    def element(self):
        e = etree.Element("token")
        e.set('name', self.name)
        if self._location is not None:
            e.append(self._location.element)

        return e

    @property
    def xml(self):
        return etree.tostring(self.element, pretty_print=True)

    @property
    def location(self):
        return self._location

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, newmap):
        self._map = newmap

    def move(self, direction, distance = 1):
        direction %= 6
        if direction < 0:
            direction += 6

        newloc = self._location + (Vector.UNIT[direction] * distance)
        if newloc not in self.map:
            raise Exception("new location %s is not in the map" % newloc)

        self._location = newloc

    def moveto(self, location):
        if self._map is None:
            raise Exception("No map set")

        if location not in self._map:
            raise Exception("Invalid location %s in map" % location)

        self._location = location
    
