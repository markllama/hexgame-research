"""
A single token on a hex board
"""

import lxml.etree as etree

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

    def move(self, direction, distance = 1):
        direction %= 6
        if direction < 0:
            direction += 6

        self._location += (Vector.UNIT[direction] * distance)

    def moveto(self, location):
        self._location = location
    
