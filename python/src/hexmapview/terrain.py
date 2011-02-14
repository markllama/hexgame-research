import logging

import hexmap

class Terrain(hexmap.Terrain):
    """
    A Terrain that knows how to draw itself when it's added to map
    """

    def repaint(self, location=None):
        """Repaint all of the terrain locations"""
        logger = logging.getLogger(self.__class__.__name__ + ".repaint")

        if location is not None:
            self.repaint_location(location)

        else:
            logger.debug("locations = %s" % self.locations)
            for location in self.locations:
                logger.debug("location = %s" % location)
                self.repaint_location(location)
