"""
A terrain on a hex map
""" 

import lxml.etree as etree

class Terrain(object):

    def __init__(self, name, locations=None, map=None):
        self.map = map
        self._name = name
        self.locations = locations

    @property
    def name(self): return self._name

    @property
    def element(self):
        e = etree.Element("terrain")
        e.set('name', self.name)
        if self.locations is not None:
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
        # Create the RIGHT terrain?
        #terrain = 
        return cls(eterrain.tag)

    
