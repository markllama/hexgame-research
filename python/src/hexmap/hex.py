"""
The Hex object
"""

class Hex():
    """
    This is a "synthetic" map object.  It is created from a Map and a Vector,
    which indicate which terrains and tokens to collect to compose the Hex.

    This allows the Map to have a single canonical view (list of Terrains and
    Tokens each with a set of locations) and not have to maintain a parallel
    set of Hex objects and all the required links.

    The down side is that changes to the Map will not be reflected in the
    hex once it's been composed.
    """


    def __init__(self, map, loc):
        self._map = map
        self._loc = loc


class TerrainList():
    """
    A synthetic list of Terrains for a Hex
    """

    def __init__(self, map, loc):
        """
        Return a list of all of the terrains at the given location
        """
    pass

class TokenList():
    """
    A synthetic list of Tokens for a Hex
    """

    

