#!/usr/bin/python
"""A simple hex map on screen"""

import os

from Tkinter import *

import hexmap

# -------------------------------------------------------------------
#
# Option Parsing and Debug/Verbose setting
#
# -------------------------------------------------------------------
from optparse import OptionParser, Option
# =========================================================================
#  Parse Command line options into global opts and fix sys.argv
# =========================================================================
# Define user controllable defaults
defaults = {
    "mapspec": None,
}

# Override defaults from environment variables (upper case) if provided
for key in defaults:
    value = os.getenv("HEXMAP_" + key.upper())
    if value is not None:
        defaults[key] = value

# Define normal control options for any script
standard_options = (
    Option("-d", "--debug", action="store_true"),
    Option("-n", "--dryrun", dest="liverun", action="store_false", default=True)
,
    Option("-v", "--verbose", action="store_true")
)

app_options = (
    Option("-m", "--mapspec", default=defaults['mapspec']),
)

all_options = standard_options + app_options

# Parse the command line argments
(opt, args) = OptionParser(option_list=all_options).parse_args()

# Push the remaining args back onto argv *AFTER* the call name (argv[0])
# web.application.run() uses argv for listener IP and port number
sys.argv[1:] = args

import logging
logging.basicConfig(level=logging.WARNING)

if opt.verbose:
    logging.root.setLevel(logging.INFO)

if opt.debug:
    logging.root.setLevel(logging.DEBUG)

if __name__ == "__main__":
    
    root = Tk()
    root.title("Hex Map")
    #root.geometry("500x500")

    borders = hexmap.BorderTerrainView(
        "border", 
        locations=[hexmap.Vector(4, 5)]
        )

    hm = hexmap.HexMapView(
        size=hexmap.Vector(15, 23),
        terrains=[borders]
        )

    hm.pack(fill=BOTH, expand=1)

    root.mainloop()
