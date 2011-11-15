"""
Add graphic elements to the hex object
"""

import logging

from hexmap import Hex as PlainHex

class Hex(PlainHex):

    def repaint(self):
        logger = logging.getLogger(self.__class__.__name__ + ".repaint")

        if self.terrains is not None:
            for terrain in self.terrains:
                logger.debug("repainting terrain %s" % terrain)
                terrain.repaint(location=self)

        if self.tokens is not None:
            for token in self.tokens:
                logger.debug("repainting token %s" % token)
                token.repaint(location=self)
