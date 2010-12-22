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
import lxml.etree as etree

from vector import Vector
from terrain import Terrain

class HexMap(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin=Vector.ORIGIN, terrains={}, tokens={}, 
                 name=None, game=None, copyright=None):

        # name
        # game
        # copyright

        self._size = size
        self._origin = origin

        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains
        self._tokens = tokens

        self._name = name
        self._game = game
        self._copyright = copyright

    # a factory from an XML map
    @staticmethod
    def fromelement(eroot):
        pass

    @staticmethod
    def fromstring(mapstring):
        pass

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
    def terrains(self): return self._terrains

    @property
    def tokens(self): return self._tokens

    def ybias(self, hx):
        return int(hx / 2)

    def hyfirst(self, hv):
        # There is no valid hy if hx is out of range
        if hv.hx < self.origin.hx or hv.hx >= self.origin.hx + self.size.hx: 
            return None

        return - self.origin.hy + self.ybias(hv.hx + self.origin.hx)

    def __contains__(self, hv):
        # check the hx boundaries

        # check the hy boundaries
        hyfirst = self.hyfirst(hv)
        if hyfirst is None: return False

        hylast = hyfirst + self.size.hy
        if hv.hy < hyfirst or hv.hy >= hylast: return False

        return True

    def addToken(self, token):
        # check that it's not already there.
        token.map = self
        token.location = None
        self._tokens.append(token)

    def removeToken(self, token):
        self._tokens.remove(token)
        token.location = None
        token.map = None
