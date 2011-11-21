#
# A single terrain
#

class Terrain():
    """
    a hex modifier
    """

    def __init__(self, name, map=None, locations=[]):
        self._name = name
        self._map = map
        self._locations = locations

    @property
    def name(self): return self._name

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def name(self): return self._name

    @property
    def locations(self): return self._locations


