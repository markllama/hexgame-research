#!/usr/bin/python
"""A simple hex map on screen"""

from Tkinter import *

import hexmap

if __name__ == "__main__":
    
    root = Tk()
    root.title("Hex Map")
    #root.geometry("500x500")

    hm = hexmap.HexMapView(hexmap.Vector(15, 23))

    hm.pack(fill=BOTH, expand=1)

    root.mainloop()
