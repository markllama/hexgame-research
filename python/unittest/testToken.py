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
from hexmap.token import Token

class TestToken(unittest.TestCase):
    
    def testToken(self):
        
        t0 = Token("heavytank")
        
        print t0.xml

        t1 = Token("commandpost")
        t1.location=Vector(12, 14)

        print t1.xml

        t2 = Token("ogremk3", location=Vector(3, 5))
        print t2.xml


if __name__ == "__main__":
    unittest.main()
