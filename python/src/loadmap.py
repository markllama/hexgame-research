#!/usr/bin/python
"""
Create a map by loading an XML file
"""

#!/usr/bin/python
"""A simple hex map on screen"""

import os

from Tkinter import *

import hexmapview

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


# Map the terrain types in the XML file to python classes
terrainmap = {
    "HexMapView.Terrain.Border": hexmapview.BorderTerrain,
    "HexMapView.Terrain.Center": hexmapview.CenterTerrain
}

# map the token types in the XML file to python classes
tokenmap = {

}

if __name__ == "__main__":
    
    print "Loading XML file: %s" % opt.mapspec


    root = Tk()
    root.title("Hex Map")
    #root.geometry("500x500")

    

    fr = Frame()

    fr.grid_rowconfigure(0, weight=1)
    fr.grid_columnconfigure(0, weight=1)

    xscrollbar = Scrollbar(fr, orient=HORIZONTAL)
    xscrollbar.grid(row=1, column=0, sticky=E+W)

    yscrollbar = Scrollbar(fr)
    yscrollbar.grid(row=0, column=1, sticky=N+S)

    mapstring = file(opt.mapspec).read()
    hm = hexmapview.Map.fromstring(fr, mapstring, terrainmap)
    
    hm.repaint()

    hm.grid(row=0, column=0, sticky=N+S+E+W)

    fr.pack(fill=BOTH, expand=1)
    
    root.mainloop()
