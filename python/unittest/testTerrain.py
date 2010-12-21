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

from hexmap.vector import Vector
from hexmap.terrain import Terrain

class TestTerrain(unittest.TestCase):
    
    def testTerrain(self):
        
        t0 = Terrain("border")
        
        print t0.xml

        t1 = Terrain("crater")
        t1.locations=[Vector(12, 14), Vector(2, 3)]

        print t1.xml

        t2 = Terrain("hedge", locations="ALL")
        print t2.xml


if __name__ == "__main__":
    unittest.main()
