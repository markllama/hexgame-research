"""
A terrain on a hex map
""" 
import logging
import collections

import lxml.etree as etree

import hexmap
from vector import Vector
import map


class Terrain(object):

    name = "terrain"

    def __init__(self, name, locations=None, depth=0, map=None):
        self._map = map
        self._name = name
        #self._type = self.__class__.name
        self._depth = depth

        if locations == "ALL":
            self._all = True
        else:
            self._all = False

        self._locations = locations or []

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def locations(self):
        return self._locations

    #@property
    #def locations(self):
    #    logger = logging.getLogger(self.__class__.__name__ + ".locations.getter")
        # if we're passed a callable, assume it's an iterator
     #   if isinstance(self._locations, collections.Callable):
     #       logger.debug("Locations is callable")
     #       return self._locations(self._map)
     #   elif isinstance(self._locations, list):
     #       logger.debug("Locations is a list")
     #       return self._locations 
     #   elif self._locations is None:
     #       logger.debug("Locations is None")
     #       return []
     #   else:
     #       raise ValueError()


    #@locations.setter
    #def locations(self, locs):
    #    logger = logging.getLogger(self.__class__.__name__ + ".locations.setter")
        # if we're passed a callable, assume it's an iterator
    #    if isinstance(locs, collections.Callable):
    #        logger.debug("Locations is callable")
    #        self._locations = locs
    #    elif isinstance(locs, list):
    #        logger.debug("Locations is a list")
    #        self._locations = locs
    #    elif locs is None:
    #        logger.debug("Locations is None")
    #        self._locations = None
    #    else:
    #        raise ValueError()

    def __contains__(self, loc):
        logger = logging.getLogger(self.__class__.__name__ + ".__contains__")

        logger.debug("checking %s in locations: %s" % (loc, self._locations))
        if self._locations is hexmap.map.AllHexes:
            return loc in self._map

        return loc in self.locations

    @property
    def name(self): return self._name
    
    @property
    def depth(self): return self._depth

    @property
    def element(self):
        e = etree.Element("terrain")
        e.set("type", self.__class__.__name__)
        try:
            e.set('name', self.name)
        except TypeError:
            print "Cannot set name to %s" % self.name
            e.set('name', 'ERROR')
        if self._all:
            e.set("all", "true")
        elif self.locations is not None:
            loclist = etree.Element("locations")
            if self._locations == map.AllHexes:
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
        logger = logging.getLogger(cls.__name__ + ".fromelement")
        t = cls(eterrain.tag)
        depth = eterrain.get("depth") or 0
        eloclist = eterrain.find("locations")
        if eloclist.get("all") == "true":
            t._locations=map.AllHexes(t)
        else:
            logger.debug("Not all hexes")
            for eloc in eloclist:
                logger.debug("new location %s" % eloc)
                vloc = Vector.fromelement(eloc)
                t.locations.append(vloc)

            logger.debug("locations: %s" % t.locations)

        return t

