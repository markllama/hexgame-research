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

from hexmap import HexMap, Vector

class TestHexMap(unittest.TestCase):

    def testHexMap(self):
        hm0 = HexMap(Vector(15, 22))

        self.assertEquals(Vector.ORIGIN, hm0.origin)
        self.assertEquals(Vector(15,22), hm0.size)
        
if __name__ == "__main__":
    unittest.main()
