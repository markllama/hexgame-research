from terrain import Terrain

class SuperHex(Terrain):
    """Draw a hex who's vertices are the centers of its neighbors"""

    def repaint_location(self, loc):
        """Draw the border around the hex's location(s)"""

        center = self._map.hexcenter(loc)
        vertices = [self._map.hexcenter(n) for n in loc.neighbors]
        coordinates = []
        for v in vertices: coordinates.extend([v.x, v.y]) 
        self._map.create_polygon(
            coordinates, 
            fill="white", 
            outline="black", 
            tag=[self.name, "terrain", "(%d,%d)" % (loc.hx, loc.hy)]
            )
