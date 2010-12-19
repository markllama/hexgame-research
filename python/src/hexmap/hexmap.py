class HexMap(object):
    """
    This represents the state of a game map
    """
    
    def __init__(self, size, origin, terrains={}, tokens={}):

        self._size = size
        self._origin = origin

        # check if the Hex constructor has been provided
        #self._hex = Hex;

        self._terrains = terrains
        self._tokens = tokens

    # a factory from an XML map
    def fromelement(eroot):
        pass

    def fromstring(mapstring):
        pass


    
class Hex(object):
    """
    """
    pass

class Terrain(object):
    pass

class Token(object):
    pass
