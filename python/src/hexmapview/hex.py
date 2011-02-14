"""
Add graphic elements to the hex object
"""

import logging

from hexmap import Hex as PlainHex

class Hex(PlainHex):

    def repaint(self):
        logger = logging.getLogger(self.__class__.__name__ + ".repaint")

        for terrain in self.terrains:
            logger.debug("repainting terrain %s" % terrain)
            terrain.repaint(location=self)

        for token in self.tokens:
            logger.debug("repainting token %s" % token)
            token.repaint(location=self)
