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

from hexmap import Vector

import unittest

class TestVector(unittest.TestCase):

    def testVector(self):

        # unit
        v0 = Vector()
        self.assertEquals(0, v0.hx)
        self.assertEquals(0, v0.hy)
        self.assertEquals(0, v0.hz)

        # two integers
        v1 = Vector(4, 5)
        self.assertEquals(4, v1.hx)
        self.assertEquals(5, v1.hy)
        self.assertEquals(1, v1.hz)

        # single vector
        v2 = Vector(v1)
        self.assertEquals(4, v2.hx)
        self.assertEquals(5, v2.hy)
        self.assertEquals(1, v1.hz)

        # two integers
        v3 = Vector(hx=12, hy=-3)
        self.assertEquals(12, v3.hx)
        self.assertEquals(-3, v3.hy)
        self.assertEquals(-15, v3.hz)

        # a single vector
        v4 = Vector(hv=v2)
        self.assertEquals(4, v4.hx)
        self.assertEquals(5, v4.hy)

    def testFromElement(self):
        e5 = etree.fromstring('<vector hx="-5" hy="14"/>')
        v5 = Vector.fromelement(e5)
        self.assertEquals(-5, v5.hx)
        self.assertEquals(14, v5.hy)

    def testFromString(self):
        v6 = Vector.fromxml('<vector hx="6" hy="-2"/>')
        self.assertEquals(6, v6.hx)
        self.assertEquals(-2, v6.hy)


    def testElement(self):
        v0 = Vector(5, 12)
        e0 = v0.element
        self.assertEqual('<vector hx="5" hy="12"/>', etree.tostring(e0))

    def testXml(self):
        v0 = Vector(-9, -4)
        s0 = v0.xml
        self.assertEqual('<vector hx="-9" hy="-4" />', s0)

    def testLen(self):
        self.assertEquals(0, len(Vector.ORIGIN))
        self.assertEquals(1, len(Vector.UNIT[0]))
        self.assertEquals(1, len(Vector.UNIT[1]))
        self.assertEquals(1, len(Vector.UNIT[2]))
        self.assertEquals(1, len(Vector.UNIT[3]))
        self.assertEquals(1, len(Vector.UNIT[4]))
        self.assertEquals(1, len(Vector.UNIT[5]))
        self.assertEquals(2, len(Vector(2, 0)))
        self.assertEquals(8, len(Vector(-5, 3)))
        self.assertEquals(12, len(Vector(6, -6)))
        self.assertEquals(8, len(Vector(-4, 4)))


    def testEqual(self):
        self.assertEquals(Vector.ORIGIN, Vector())
        self.assertEquals(Vector.UNIT[0], Vector(Vector.UNIT[0]))
        self.assertEquals(Vector.UNIT[3], Vector(Vector.UNIT[3]))


    def testAdd(self):
        v0 = Vector(12, 15)
        v1 = Vector(2, 3)
        v2 = Vector(10, 12)

        self.assertEquals(Vector.UNIT[0], Vector.ORIGIN + Vector.UNIT[0])
        self.assertEquals(v0, v1 + v2)

        self.assertEquals(Vector(3, 2), Vector(8, 5) + Vector(-5, -3))

    def testSub(self):
        v0 = Vector(12, 15)
        v1 = Vector(2, 3)
        v2 = Vector(10, 12)
        
        self.assertEquals(Vector.UNIT[3], Vector.ORIGIN - Vector.UNIT[0])
        self.assertEquals(Vector(-8, -9), v1 - v2)

        self.assertEquals(Vector(13, 8), Vector(8, 5) - Vector(-5, -3))


    def testMul(self):
        self.assertEquals(Vector(0, -3), Vector.UNIT[0] * 3)
        self.assertEquals(Vector(6, -15), Vector(2, -5) * 3)

    def testDistance(self):
        self.assertEquals(0, Vector.ORIGIN.distance(Vector.ORIGIN))
        self.assertEquals(0, Vector.UNIT[3].distance(Vector.UNIT[3]))
        self.assertEquals(0, Vector.UNIT[5].distance(Vector.UNIT[5]))
        self.assertEquals(0, Vector(12, 14).distance(Vector(12, 14)))

        self.assertEquals(1, Vector.UNIT[0].distance(Vector.ORIGIN))
        self.assertEquals(1, Vector.UNIT[1].distance(Vector.ORIGIN))
        self.assertEquals(1, Vector.UNIT[2].distance(Vector.ORIGIN))
        self.assertEquals(1, Vector.UNIT[3].distance(Vector.ORIGIN))
        self.assertEquals(1, Vector.UNIT[4].distance(Vector.ORIGIN))
        self.assertEquals(1, Vector.UNIT[5].distance(Vector.ORIGIN))

        self.assertEquals(10, Vector(5, 0).distance(Vector(-5, 0)))

    def testHextant(self):

        self.assertEquals(0, Vector.UNIT[0].hextant)
        self.assertEquals(1, Vector.UNIT[1].hextant)
        self.assertEquals(2, Vector.UNIT[2].hextant)
        self.assertEquals(3, Vector.UNIT[3].hextant)
        self.assertEquals(4, Vector.UNIT[4].hextant)
        self.assertEquals(5, Vector.UNIT[5].hextant)

        self.assertEquals(0, (Vector.UNIT[0] * 5).hextant)
        self.assertEquals(0, ((Vector.UNIT[0] * 5) + Vector.UNIT[1]).hextant)

        self.assertEquals(1, Vector(5, 1).hextant)
        self.assertEquals(3, Vector(-1, 6).hextant)
        self.assertEquals(3, Vector(-5, 6).hextant)
        self.assertEquals(4, Vector(-6, 0).hextant)
        self.assertEquals(4, Vector(-6, -1).hextant)
        self.assertEquals(5, Vector(-1, -6).hextant)

    def testRotate(self):
        v0 = Vector(-1, -5)
        
        self.assertEquals(v0, v0.rotate(0))
        self.assertEquals(Vector(4, -1), v0.rotate(1))
        self.assertEquals(Vector(5, 4), v0.rotate(2))
        self.assertEquals(Vector(1, 5), v0.rotate(3))
        self.assertEquals(Vector(-4, 1), v0.rotate(4))
        self.assertEquals(Vector(-5, -4), v0.rotate(5))
        self.assertEquals(v0, v0.rotate(6))
        self.assertEquals(v0, v0.rotate(-6))
        self.assertEquals(Vector(-5, -4), v0.rotate(-1))


    def testBearing(self):

        v0 = Vector(-1, -5)
        
        self.assertEquals(5.8, v0.bearing)

    def testNeighbors(self):

        v0 = Vector(5, 8)
        neighbors = [
            Vector(5, 7),
            Vector(6, 8),
            Vector(6, 9),
            Vector(5, 9),
            Vector(4, 8),
            Vector(4, 7)
            ]

        self.assertEquals(neighbors, v0.neighbors)
        
if __name__ == "__main__":
    unittest.main()

