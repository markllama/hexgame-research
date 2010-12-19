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


import xml.etree.ElementTree as etree

from hexmap.vector import Vector

import unittest

class TestVector(unittest.TestCase):

    def testVector(self):

        # unit
        v0 = Vector()
        self.assertEquals(0, v0.hx)
        self.assertEquals(0, v0.hy)

        # two integers
        v1 = Vector(4, 5)
        self.assertEquals(4, v1.hx)
        self.assertEquals(5, v1.hy)

        # single vector
        v2 = Vector(v1)
        self.assertEquals(4, v2.hx)
        self.assertEquals(5, v2.hy)

        # two integers
        v3 = Vector(hx=12, hy=-3)
        self.assertEquals(12, v3.hx)
        self.assertEquals(-3, v3.hy)

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

if __name__ == "__main__":
    unittest.main()

