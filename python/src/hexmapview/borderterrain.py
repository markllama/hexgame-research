from terrain import Terrain

class BorderTerrain(Terrain):
    """Draw the hex shape around the center"""

    def repaint_location(self, loc):
        """Draw the border around the hex's location(s)"""

        center = self._map.hexcenter(loc)
        vertices = self._map.hexvertices(loc)
        coordinates = []
        for v in vertices: coordinates.extend([v.x, v.y]) 
        self._map.create_polygon(
            coordinates, 
            fill="white", 
            outline="black", 
            tag=[self.name, "(%d,%d)" % (loc.hx, loc.hy)]
            )
