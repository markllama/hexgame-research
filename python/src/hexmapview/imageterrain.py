#

from terrain import Terrain

class ImageTerrain(Terrain):
    """
    A generic terrain view that 
    """
    def repaint_location(self, loc):
        """Draw the image inside the hex"""
        center = self._map.hexcenter(loc)
        side = self._map.hexradius
        self._map.create_image(center.x, center.y)
        
