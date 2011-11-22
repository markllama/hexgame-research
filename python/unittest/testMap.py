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

from hexmap import Vector, Map, Terrain, Token

import unittest

class TestMap(unittest.TestCase):
    
    # constructor
    def testMap(self):

        m0 = Map()
        self.assertTrue(isinstance(m0, Map))

        self.assertEqual('unset', m0.name)
        self.assertEqual(Vector(15,22), m0.size)
        self.assertEqual(Vector.ORIGIN, m0.origin)

    def testMapConstructorXMLString(self):
        pass

    def testMapConstructorURLString(self):
        pass

    def testMapConstructorDocument(self):
        pass

    def testMapConstructorElement(self):
        pass

    def testMapConstuctorVector(self):
        pass

    def testMapConstructorInteger(self):
        pass

    def testMapOrigin(self):
        m0 = Map(origin=Vector(5, 8))

        self.assertEqual(5, m0.origin.hx)
        self.assertEqual(8, m0.origin.hy)

    def testMapHxFirst(self):

        m0 = Map(size=Vector(7, 7), origin=Vector(0, 0))
        m1 = Map(size=Vector(7, 7), origin=Vector(-3, -3))
        self.assertEqual(0, m0.hxfirst())
        self.assertEqual(-3, m1.hxfirst())

    def testMapHxCount(self):
        m0 = Map(size=Vector(7, 7), origin=Vector(0, 0))
        m1 = Map(size=Vector(9, 4), origin=Vector(-3, -3))
        self.assertEqual(7, m0.hxcount())
        self.assertEqual(9, m1.hxcount())

    def testMapYBias(self):
        map0 = Map(size=Vector(6, 6), origin=Vector(0, 0))
        map1 = Map(size=Vector(7, 7), origin=Vector(-3, -3))

        self.assertEqual(-1, map0.ybias(-1), "map 0 bias -1 = -1");
        self.assertEqual(0, map0.ybias(0), "map 0 bias 0 = 0");
        self.assertEqual(0, map0.ybias(1), "map 0 bias 1 = 0");
        self.assertEqual(1, map0.ybias(2), "map 0 bias 2 = 1");
        self.assertEqual(1, map0.ybias(3), "map 0 bias 3 = 1");
        self.assertEqual(2, map0.ybias(4), "map 0 bias 4 = 2");
        self.assertEqual(2, map0.ybias(5), "map 0 bias 5 = 2");
        self.assertEqual(3, map0.ybias(6), "map 0 bias 6 = 3");

        self.assertEqual(-1, map1.ybias(-4), "map 1 bias -4 = -1");
        self.assertEqual(0, map1.ybias(-3), "map 1 bias -3 = 0");
        self.assertEqual(0, map1.ybias(-2), "map 1 bias -2 = 0");
        self.assertEqual(1, map1.ybias(-1), "map 1 bias -1 = 1");
        self.assertEqual(1, map1.ybias(0), "map 1 bias 0 = 1");
        self.assertEqual(2, map1.ybias(1), "map 1 bias 1 = 2");
        self.assertEqual(2, map1.ybias(2), "map 1 bias 2 = 2");
        self.assertEqual(3, map1.ybias(3), "map 1 bias 3 = 3");
        self.assertEqual(3, map1.ybias(4), "map 1 bias 4 = 3");

    def testMapHyFirst(self):

        map0 = Map(size=Vector(6, 6), origin=Vector(0, 0));
        map1 = Map(size=Vector(7, 7), origin=Vector(-3, -3));

        self.assertEqual(None, map0.hyfirst(-1), "map 0 hyfirst(-1) = None")
        self.assertEqual(0, map0.hyfirst(0), "map 0 hyfirst(0) = 0")
        self.assertEqual(0, map0.hyfirst(1), "map 0 hyfirst(1) = 0")
        self.assertEqual(1, map0.hyfirst(2), "map 0 hyfirst(2) = 1")
        self.assertEqual(1, map0.hyfirst(3), "map 0 hyfirst(3) = 1")
        self.assertEqual(2, map0.hyfirst(4), "map 0 hyfirst(4) = 2")
        self.assertEqual(2, map0.hyfirst(5), "map 0 hyfirst(5) = 2")
        self.assertEqual(None, map0.hyfirst(6), "map 0 hyfirst(6) = None")

        self.assertEqual(None, map1.hyfirst(-4), "map 1 hyfirst(-4) = None")
        self.assertEqual(-3, map1.hyfirst(-3), "map 1 hyfirst(-3) = -3")
        self.assertEqual(-3, map1.hyfirst(-2), "map 1 hyfirst(-2) = -3")
        self.assertEqual(-2, map1.hyfirst(-1), "map 1 hyfirst(-1) = -2")
        self.assertEqual(-2, map1.hyfirst(0), "map 1 hyfirst(0) = -2")
        self.assertEqual(-1, map1.hyfirst(1), "map 1 hyfirst(1) = -1")
        self.assertEqual(-1, map1.hyfirst(2), "map 1 hyfirst(2) = -1")
        self.assertEqual(0, map1.hyfirst(3), "map 1 hyfirst(3) = 0")
        self.assertEqual(None, map1.hyfirst(4), "map 1 hyfirst(4) = None")

    def testMapContains(self):

        map0 = Map(size=Vector(6, 6), origin=Vector(0, 0));

        # check the internal corners
        self.assertTrue(map0.contains(Vector.ORIGIN), "map 0 contains origin")
        self.assertTrue(map0.contains(Vector(0, 5)), "map 0 contains 0, 5")
        self.assertTrue(map0.contains(Vector(5, 2)), "map 0 contains 5, 2")
        self.assertTrue(map0.contains(Vector(5, 7)), "map 0 contains 5, 7")

        # check the external corners
        self.assertFalse(map0.contains(Vector(-1, -1)), "map 0 not -1, -1")
        self.assertFalse(map0.contains(Vector(-1, 0)), "map 0 not -1, 0")
        self.assertFalse(map0.contains(Vector(0, -1)), "map 0 not 0, -1")

        # check the external corners
        self.assertFalse(map0.contains(Vector(-1, 5)), "map 0 not -1, 5")
        self.assertFalse( map0.contains(Vector(-1, 6)), "map 0 not -1, 6")
        self.assertFalse( map0.contains(Vector(0, 6)), "map 0 not 0, 6")

        self.assertFalse(map0.contains(Vector(5, 1)), "map 0 not 5, 1") 
        self.assertFalse(map0.contains(Vector(6, 2)), "map 0 not 6, 2")
        self.assertFalse(map0.contains(Vector(6, 3)), "map 0 not 6, 3")

        self.assertFalse(map0.contains(Vector(5, 8)), "map 0 not 5, 8")
        self.assertFalse( map0.contains(Vector(6, 7)), "map 0 not 6, 7")
        self.assertFalse( map0.contains(Vector(6, 8)), "map 0 not 6, 8")


    def testMapAddTerrain(self):
        """
        
        """

        m0 = Map(size=Vector(6,5))

        # add a valid terrain
        t0 = Terrain(name="t0")
        m0.addTerrain(t0)
        self.assertEqual(1, len(m0.terrains))
        self.assertEqual(m0, t0.map)

        # try adding an invalid terrain?
        self.assertRaises(TypeError, m0.addTerrain, 2)

    def testMapAddToken(self):
        """
        
        """

        m0 = Map(size=Vector(6,5))

        # add a valid terrain
        t0 = Token(name="t0")
        m0.addToken(t0)
        self.assertEqual(1, len(m0.tokens))
        self.assertEqual(m0, t0.map)

        # try adding an invalid terrain?
        self.assertRaises(TypeError, m0.addToken, 2)

    def testMapGetHex(self):
        self.fail("Pending")

    def testMapIterator(self):
        self.fail("Pending")


if __name__ == "__main__":
    unittest.main()

