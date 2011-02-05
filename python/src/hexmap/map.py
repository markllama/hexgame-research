"""

<map xmls="lamourine.homeunix.org/hexmap" name="sample" >
  <copyright>GPL</copyright>
  <size><vector hx="15" hy="22" /></size>
  <origin><vector hx="0" hy="0" /></origin>
  <terrains>
     <terrain name="border">
       <locations all="true" />
     <terrain>
  </terrains>
  <tokens>
     <token type="hvytank">
       <locations>
         <vector hx="6" hy="10" />
       </locations>
     </token>
  </tokens>
</map>
"""

import logging

import lxml.etree as etree

from vector import Vector
from terrain import Terrain

class MapError(Exception): pass

class Map(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None):

        logger = logging.getLogger(self.__class__.__name__ + ".__init__")
        # name
        # game
        # copyright

        self._size = size
        self._origin = origin
        logger.debug("New hex map origin = %s" % self._origin)
        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains
        
        for terrain in self._terrains:
                terrain._map = self

        self._tokens = tokens or []
        #for token in tokens:
        #    token.map = self

        self._name = name
        self._game = game
        self._copyright = copyright

    # a factory from an XML map
    @classmethod
    def fromelement(cls, maptree, terrainmap=None, tokenmap=None):
        
        # get the size
        esize = maptree.find("size")
        if esize is None:
            raise MapError("A map must have a size")
        else:
            evec = esize[0]
            size = Vector.fromelement(evec)


        # and the origin
        eorigin = maptree.find("origin")
        if eorigin is not None:
            evec = eorigin[0]
            origin = Vector.fromelement(evec) 
        else:
            origin = Vector.ORIGIN

        # and the name, game and copyright
        hm = cls(size, origin)

        # add the terrains
        for eterrain in maptree.findall("terrain"):
            tname = eterrain.get("type")
            if tname in terrainmap:
                terrain = terrainmap[tname].fromelement(eterrain)
                hm.addTerrain(terrain)
            else:
                print "terrain name %s not in terrain map %s" % (tname, terrainmap)

        return hm

    @classmethod
    def fromstring(cls, mapstring, terrainmap=None, tokenmap=None):
        maptree = etree.fromstring(mapstring)
        return cls.fromelement(maptree, terrainmap, tokenmap)

    @property
    def element(self):
        e = etree.Element("map")
        if self.name:
            e.set('name', self.name)
        
        if self.copyright:
            e.set("copyright", self.copyright)

        s = etree.Element("size")
        s.append(self.size.element)
        e.append(s)

        if self.origin is not None:
            o = etree.Element("origin")
            o.append(self.origin.element)
            e.append(o)
            
        if len(self.terrains) > 0:
            tlist = etree.Element("terrains")
            for t in self.terrains:
                tlist.append(t.element)
            e.append(tlist)

        if len(self.tokens) > 0:
            tlist = etree.Element("tokens")
            for t in self.tokens:
                tlist.append(t.element)
            e.append(tlist)

        return e

    @property
    def xml(self):
        return etree.tostring(self.element, pretty_print=True)

    @property
    def size(self): return self._size

    @property
    def origin(self): return self._origin

    @property
    def name(self): return self._name

    @property
    def game(self): return self._game

    @property
    def copyright(self): return self._copyright

    @property
    def terrains(self):
        if self._terrains is True:
            return AllTerrains(self)
        if self._terrains is None:
            return []
        return self._terrains

    @property
    def tokens(self): return self._tokens

    def ybias(self, hx):
        return int(hx / 2)

    def hyfirst(self, hx):
        # There is no valid hy if hx is out of range
        if hx < -self.origin.hx or hx >= -self.origin.hx + self.size.hx: 
            return None

        return - self.origin.hy + self.ybias(hx + self.origin.hx)

    def __contains__(self, hv):
        # check the hx boundaries

        # check the hy boundaries
        hyfirst = self.hyfirst(hv.hx)
        if hyfirst is None: return False

        hylast = hyfirst + self.size.hy
        if hv.hy < hyfirst or hv.hy >= hylast: return False

        return True

    def addTerrain(self, terrain):
        self._terrains.append(terrain)
        terrain.map = self
        
    def addToken(self, token):
        # check that it's not already there.
        token.map = self
        token._location = None
        self._tokens.append(token)

    def removeToken(self, token):
        self._tokens.remove(token)
        token._location = None
        token.map = None

    def __iter__(self):
        return AllHexes(self)

    @property
    def allhexes(self):
        return AllHexes(self)

class AllHexes(object):
    
    def __init__(self, hm):
        self._hexmap = hm
        self._current = None

    def __iter__(self): return self

    def next(self):


        if self._current is None:
            """Set and return the first hex"""
            hx = self._hexmap.origin.hx
            hy = self._hexmap.hyfirst(hx)
            self._current = Vector(hx, hy)
            return self._current

        """Step to the next location"""
        next = self._current + Vector.UNIT[3]
        if next in self._hexmap:
            self._current = next
            return self._current

        # step to the next column
        hx = next.hx + 1
        hy = self._hexmap.hyfirst(hx)
        next = Vector(hx, hy)
        if next in self._hexmap:
            self._current = next
            return self._current

        raise StopIteration
