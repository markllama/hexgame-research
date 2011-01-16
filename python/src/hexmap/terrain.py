"""
A terrain on a hex map
""" 

import lxml.etree as etree

from hexmap import Vector

class Terrain(object):

    name = "terrain"

    def __init__(self, name, locations=None, map=None):
        self._map = map
        self._name = self.__class__.name
        self._all = False
        self.locations = locations or []

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def name(self): return self._name
    
    @property
    def element(self):
        e = etree.Element("terrain")
        e.set("type", self.__class__.__name__)
        e.set('name', self.name)
        if self._all:
            e.set("all", "true")
        elif self.locations is not None:
            loclist = etree.Element("locations")
            if self.locations == "ALL":
                loclist.set("all", "true")
            else:
                for l in self.locations:
                    loclist.append(l.element)

            e.append(loclist)

        return e

    @property
    def xml(self):
        return etree.tostring(self.element, pretty_print=True)

    @classmethod
    def fromstring(cls, xmlstring):
        element = etree.fromstring(xmlstring)
        return cls.fromelement(element)

    @classmethod
    def fromelement(cls, eterrain):
        t = cls(eterrain.tag)
        eloclist = eterrain.find("locations")
        if eloclist.get("all") == "true":
            t._all = True
        else:
            for eloc in eloclist:
                vloc = Vector.fromelement(eloc)
                t.locations.append(vloc)

        return t
