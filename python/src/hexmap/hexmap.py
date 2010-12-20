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
        
        s = etree.Element("size")
        s.append()

    @property
    def xml(self):
        pass

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


