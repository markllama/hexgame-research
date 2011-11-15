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

if __name__ == "__main__":
    
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

    borders = hexmapview.BorderTerrain("border", locations=hexmapview.AllHexes)
    centers = hexmapview.CenterTerrain("center", locations=hexmapview.AllHexes)

    hm = hexmapview.Map(
        fr,
        name="simple",
        size=hexmapview.Vector(15, 22),
        terrains=[borders, centers],
        hexrun=15
        )

    print "map name = %s (%s)" % (hm.name, hm._name)
    
    hm.repaint()

    hm.config(xscrollcommand=xscrollbar.set)
    hm.config(yscrollcommand=yscrollbar.set)

    xscrollbar.config(command=hm.xview)
    yscrollbar.config(command=hm.yview)

    def pressedWhere(event):

        framepoint = hexmapview.Point(event.x, event.y)
        canvaspoint = hm.canvaspoint(framepoint)
        hc = hm.point2hex(canvaspoint)
        print "You clicked on canvas(%d,%d), Thats in hex%s" % \
            (canvaspoint.x, canvaspoint.y, hc)

        idlist = hm.find_withtag(CURRENT)
        idlist += hm.find_below(idlist[0])
        print "there are %d items there" % len(idlist)
        for id in idlist:
            print "-- " + str(hm.gettags(id))

    hm.bind('<Button-1>', pressedWhere)

    hm.grid(row=0, column=0, sticky=N+S+E+W)

    fr.pack(fill=BOTH, expand=1)

    #print [hex for hex in hm]
    #print "--- starting ---"

    #print hm.xml

    circle = PhotoImage("data/circle.png")
    imageitem = hm.create_image(200, 200, image=circle, tags=['image', 'circle'], state=NORMAL)

    h = hexmapview.Hex(4, 4, map=hm)
    print h.terrains
    print h.tokens
    print h
    
    root.mainloop()
