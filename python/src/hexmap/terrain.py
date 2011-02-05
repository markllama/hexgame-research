"""
A terrain on a hex map
""" 
import logging
import collections

import lxml.etree as etree

from hexmap import Vector

class Terrain(object):

    name = "terrain"

    def __init__(self, name, locations=None, map=None):
        self._map = map
        self._name = self.__class__.name

        if locations == "ALL":
            self._all = True
        else:
            self._all = False

        self.locations = locations

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def locations(self):
        logger = logging.getLogger(self.__class__.__name__ + ".locations.getter")
        # if we're passed a callable, assume it's an iterator
        if isinstance(self._locations, collections.Callable):
            logger.debug("Locations is callable")
            return self._locations(self._map)
        elif isinstance(self._locations, list):
            logger.debug("Locations is a list")
            return self._locations 
        elif self._locations is None:
            logger.debug("Locations is None")
            return []
        else:
            raise ValueError()


    @locations.setter
    def locations(self, locs):
        logger = logging.getLogger(self.__class__.__name__ + ".locations.setter")
        # if we're passed a callable, assume it's an iterator
        if isinstance(locs, collections.Callable):
            logger.debug("Locations is callable")
            self._locations = locs
        elif isinstance(locs, list):
            logger.debug("Locations is a list")
            self._locations = locs
        elif locs is None:
            logger.debug("Locations is None")
            self._locations = None
        else:
            raise ValueError()
        
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

