import hexmap

class Terrain(hexmap.Terrain):
    """
    A Terrain that knows how to draw itself when it's added to map
    """

    def repaint(self):
        """Repaint all of the terrain locations"""

        for l in self.locations:
            self.repaint_location(l)


