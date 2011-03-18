from terrain import Terrain

class Vertex(Terrain):
    """Draw at the corner of a SuperBorder hex"""

    def __init__(self, name, locations=None, map=None, color="black"):
        Terrain.__init__(self, name, locations, map)
        self._color = color

    def repaint_location(self, loc):
        center = self._map.hexcenter(loc)
        vertices = [center.x - 4, center.y - 4, center.x + 4, center.y + 4]
        self._map.create_rectangle(
            vertices, 
            fill=self._color,
            tag = [self.name, "terrain", "(%d,%d)" % (loc.hx, loc.hy)]
            )
                                   
