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

class HexMapError(Exception): pass

class HexMap(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin=Vector.ORIGIN, terrains=None, tokens=None, 
                 name=None, game=None, copyright=None):

        # name
        # game
        # copyright

        self._size = size
        self._origin = origin

        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains or []
        self._tokens = tokens or []

        self._name = name
        self._game = game
        self._copyright = copyright

    # a factory from an XML map
    @staticmethod
    def fromelement(maptree, terrainmap=None, tokenmap=None):
        
        # get the size
        esize = maptree.find("size")
        if esize is None:
            raise HexMapError("A map must have a size")
        else:
            evec = esize[0]
            size = Vector.fromelement(evec)


        # and the origin
        eorigin = maptree.find("origin")
        if eorigin is not None:
            evec = eorigin[0]
            origin = Vector.fromelement(evec) 
        else:
            origin = None

        # and the name, game and copyright
        hm = HexMap(size, origin)

        # add the terrains
        for eterrain in maptree.findall("terrain"):
            tname = eterrain.get("type")
            if tname in terrainmap:
                terrain = terrainmap[tname].fromelement(eterrain)
                hm.addTerrain(terrain)
            else:
                print "terrain name %s not in terrain map %s" % (tname, terrainmap)

        return hm

    @staticmethod
    def fromstring(mapstring, terrainmap=None, tokenmap=None):
        maptree = etree.fromstring(mapstring)
        return HexMap.fromelement(maptree, terrainmap, tokenmap)

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


    def addTerrain(self, terrain):
        self._terrains.append(terrain)
        terrain.map = self
        
