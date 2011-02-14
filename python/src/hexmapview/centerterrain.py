from terrain import Terrain

class CenterTerrain(Terrain):
    """Draw a dot in the center of the hex"""

    def __init__(self, name, locations=None, map=None, color="black"):
        Terrain.__init__(self, name, locations, map)
        self._color = color

    def repaint_location(self, loc):
        center = self._map.hexcenter(loc)
        vertices = [center.x - 1, center.y - 1, center.x - 1, center.y + 1]
        self._map.create_rectangle(
            vertices, 
            fill=self._color,
            tag = [self.name, "terrain", "(%d,%d)" % (loc.hx, loc.hy)]
            )
                                   
