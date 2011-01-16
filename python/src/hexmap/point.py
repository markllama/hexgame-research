"""
A cartesian point
"""

import math
import lxml.etree as etree

class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def __len__(self):
        return round(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

    def __add__(self, other):
        assert(isinstance(other, Point))
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert(isinstance(other, Point))
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        assert(isinstance(other, int))
        return Point(self.x * other, self.y * other)

    def __div__(self, other):
        assert(isinstance(other, int))
        assert(other != 0)
        return Point(int(self.x / other), int(self.y / other))
        
    @property
    def element(self):
        e = etree.Element("point")
        e.set("x", self.x)
        e.set("y", self.y)

    @property
    def xml(self): 
        return etree.tostring(self.element, pretty_print=True)

    @classmethod
    def fromelement(cls, element):
        x = int(element.get("x"))
        y = int(element.get("y"))
        return cls(x, y)

    def fromxml(cls, xmlstring):
        element = etree.fromstring(xmlstring)
        return cls.fromelement(element)
