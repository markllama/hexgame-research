#!/usr/bin/python
"""

"""

import logging
logging.basicConfig(level=logging.WARNING)

import sys
from optparse import OptionParser, Option

defaults = {}

for key in defaults:
    value = os.getenv(key.upper())
    if value is not None:
        defaults[key] = value

default_options = (
    Option("-d", "--debug", action="store_true"),
    Option("-v", "--verbose", action="store_true"),
    Option("-n", "--dryrun", dest="liverun", action="store_false", default=True)
    )

application_options = (

)

all_options = default_options + application_options

(opt, args) = OptionParser(option_list=all_options).parse_args()
sys.argv[1:] = args

if opt.verbose:
    logging.root.setLevel(logging.INFO)

if opt.debug:
    logging.root.setLevel(logging.DEBUG)

#import xml.etree.ElementTree as etree
import lxml.etree as etree

import unittest

from hexmap import HexMap, Vector, Token

class TestHexMap(unittest.TestCase):

    def testHexMap(self):
        hm0 = HexMap(Vector(15, 22), name="Sample", copyright="GPL")

        self.assertEquals(Vector.ORIGIN, hm0.origin)
        self.assertEquals(Vector(15,22), hm0.size)

    def testElement(self):
        hm0 = HexMap(Vector(15, 22), name="Sample", copyright="GPL")

        e = hm0.element
        print etree.tostring(e, pretty_print=True)


    def testDimensions(self):

        hm0 = HexMap(Vector(6,8))
        self.assertEquals(None, hm0.hyfirst(Vector(-1, 0)))
        self.assertEquals(0, hm0.hyfirst(Vector(0, 0)))
        self.assertEquals(1, hm0.hyfirst(Vector(3, 0)))
        self.assertEquals(2, hm0.hyfirst(Vector(5, 0)))
        self.assertEquals(None, hm0.hyfirst(Vector(6, 0)))

    def testContains(self):

        hm0 = HexMap(Vector(6,8))

        self.assertEquals(False, Vector(-1, 2) in hm0)
        
        self.assertEquals(False, Vector(0, -1) in hm0)
        self.assertEquals(True, Vector(0, 0) in hm0)
        self.assertEquals(True, Vector(0, 7) in hm0)
        self.assertEquals(False, Vector(0, 8) in hm0)

        self.assertEquals(False, Vector(5, 1) in hm0)
        self.assertEquals(True, Vector(5, 2) in hm0)
        self.assertEquals(True, Vector(5, 9) in hm0)
        self.assertEquals(False, Vector(5, 10) in hm0)

        self.assertEquals(False, Vector(6, 4) in hm0)

        # add tests with alternate origin

    def testAddToken(self):
        hm0 = HexMap(Vector(6,8))

        t0 = Token("dummy1")

        hm0.addToken(t0)

        self.assertEquals(t0, hm0.tokens[0])
        self.assertEquals(None, t0.location)
        self.assertEquals(hm0, t0.map)

        del hm0
        del t0

    def testDelToken(self):
        hm1 = HexMap(Vector(6,8))

        t0 = Token("dummy")

        self.assertEquals(0, len(hm1.tokens))
        hm1.addToken(t0)
        self.assertEquals(1, len(hm1.tokens))
        self.assertEquals(hm1, t0.map)
        self.assertEquals(None, t0.location)

        t0.moveto(Vector(0, 0))
        self.assertEquals(Vector.ORIGIN, t0.location)
        
        try:
            t0.moveto(Vector(-1, 0))

        except:
            pass

        self.assertEquals(Vector.ORIGIN, t0.location)

        t0.move(1)
        self.assertEquals(Vector.UNIT[1], t0.location)

        hm1.removeToken(t0)
        self.assertEquals(0, len(hm1.tokens))
        self.assertEquals(None, t0.map)
        self.assertEquals(None, t0.location)


if __name__ == "__main__":
    unittest.main()
