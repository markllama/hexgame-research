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

from hexmap import Vector, Map

import unittest

class TestMap(unittest.TestCase):
    
    # constructor
    def testMap(self):

        m0 = Map()
        self.assertTrue(isinstance(m0, Map))

        self.assertEquals(None, m0.name)
        self.assertEquals(Vector(15,22), m0.size)
        self.assertEquals(Vector.ORIGIN, m0.origin)

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
        pass

    def testMapHxFirst(self):
        pass

    def testMapHxCount(self):
        pass

    def testMapHyFirst(self):
        pass

    def testMapYBias(self):
        pass

    def testMapContains(self):
        pass

    def testMapGetHex(self):
        pass

    def testMapIterator(self):
        pass


if __name__ == "__main__":
    unittest.main()

