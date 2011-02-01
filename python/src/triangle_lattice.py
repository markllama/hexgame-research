#!/usr/bin/python
"""Generate a triangular lattice in a rectangular frame"""

class Vector(object):

    def __init__(self, hx, hy):
        self.hx = hx
        self.hy = hy

    def __str__(self):
        return "(%d, %d)" % (self.hx, self.hy)

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

from Tkinter import *


import math

def sine60(a):
    return a * 8660 / 10000

mapdimensions = "550x550"

hexrun = 50
hexradius = hexrun * 2
hexwidth = hexradius * 2
hexrise = sine60(hexradius)
hexheight = hexrise * 2

mapradius = 1

porigin0 = Point(hexwidth, hexrise)
porigin = Point(250, 250)

def vertices(p):
    # expects a Point
    # Returns a list of x,y pairs for canvas.create_polygon
    return (p.x + hexradius, p.y,
            p.x + hexrun, p.y + hexrise,
            p.x - hexrun, p.y + hexrise,
            p.x - hexradius, p.y,
            p.x - hexrun, p.y - hexrise, 
            p.x + hexrun, p.y - hexrise,
            p.x + hexradius, p.y
            )

def rectangle(p0):
    # Given the center point of a hex, find the vertices of the rectangle
    # which defines the boundaries
    # These rectangles fill the plane completely in the same way that the
    # hexagons do.

    v0 = Point(p0.x - hexwidth, p0.y - hexrise)
    v1 = Point(v0.x, p0.y + hexrise)
    v2 = Point(p0.x + hexrun, v1.y)
    v3 = Point(v2.x, v0.y)
    return(v0, v1, v2, v3)

def hex2point(h, origin=Point(0, 0)):
    px = (h.hx * hexrun * 3)
    py = (h.hy * hexheight) - ((h.hx * hexheight) / 2) 
    return Point(px + origin.x, py + origin.y)

def refhex(p):
    # generate the base hex which contains a given point
    # offset by the porigin + 1/2 hex ( to get the origin hex on the
    # canvas
    hx = ((p.x - porigin.x) + hexradius) / (hexrun * 3)
    hy = ((p.y - porigin.y) + ((hx + 1) * hexrise)) / hexheight
    return Vector(hx, hy)

def point2hex(p):
    # Find the reference hex containing this point
    h = refhex(p)

    # find the center of that hex
    c = hex2point(h, porigin)

    # get the bounding rectangle of the expected hex
    r = rectangle(c)

    # find the point inside a normalized rectangle
    # offset by hexradius to make further tests easier
    # the axis point is placed at 0,0 of the normalized rectangle containing
    # the point
    np = Point(p.x - r[0].x - hexradius, p.y - r[0].y - hexrise)
    print "np = %s: hexwidth = %s" % (np , hexradius)

    if np.x <= hexrun and np.x * 2 < abs(np.y):
        if np.y > 0:
            # step UNIT[4]
            h.hx -= 1
        else:
            # steop UNIT[5]
            h.hx -= 1
            h.hy -= 1

    return h

    
    # now adjust h if p lies in the upper or lower right triangles
    return h

def pressedWhere(event):
    h = point2hex(Point(event.x, event.y))
    print "You clicked on pixel(%d, %d).  Thats in hex%s" % (event.x, event.y, h)

class MenuBar(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master, relief=RAISED, borderwidth=1)
        mb_file = Menubutton(self, text='File')
        mb_file.pack(side=LEFT)

        mb_file.menu = Menu(mb_file)
        mb_file.menu.add_command(label="Open")
        mb_file.menu.add_command(label="Quit", command=master.quit)

        mb_edit = Menubutton(self, text="Edit")
        mb_edit.pack(side=LEFT)
        mb_edit.menu = Menu(mb_edit)
        mb_edit.menu.add_command(label="Cut")
        mb_edit.menu.add_command(label="Copy")
        mb_edit.menu.add_command(label="Paste")


        mb_help = Menubutton(self, text="Help")
        mb_help.pack(side=RIGHT)

        mb_file['menu'] = mb_file.menu
        mb_edit['menu'] = mb_edit.menu

        master.config(menu=self)



class TriMap(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.configure(width=600, height=600)
        self.createWidgets()

    def createWidgets(self):
        canvas = Canvas(self)
        canvas.bind('<Button-1>', pressedWhere)
        canvas.pack(fill=BOTH,expand=1)

	# create a rectangular array        
        hexlist = self.hexagon(mapradius, porigin)

        colors = ('yellow', 'blue', 'green', 'pink', 'brown', 'red', 'white')


        for hex in hexlist:
            p = hex['p']
            canvas.create_polygon(vertices(p), outline='black', fill=colors[hex['hextant']])
            canvas.create_text(p.x, p.y, text=str(hex['h']))

            
    def hexagon(self, radius, origin=Point(0, 0)):
        # create a full circle
        result = [{'h': Vector(0, 0), 'p': origin, 'hextant': 6}]
        for circle in range(1,radius+1):
            print "creating hexes with length " + str(circle)
       
            for hex in range(0, circle):
                hx = hex
                hy = -circle + hex 
                hz = -circle

                hexloop = (hx, hy, hz, -hx, -hy, -hz, hx)
                for hextant in range(0,6):
                    h = Vector(hexloop[hextant], hexloop[hextant+1])
                    p = hex2point(h, origin)
                    print "creating node (%d, %d): %s" % (h.hx, h.hy, str(p))
                    result.append({'h': h, 'p': p,'hextant': hextant})


        return result

if __name__ == "__main__":

    root = Tk()
    root.title('Tri Lattace')
    root.geometry(mapdimensions)

#    menubar = MenuBar(root)
#    menubar.pack(side=TOP)
    map = TriMap(root)
    map.pack(fill=BOTH, expand=1)
#    root.config(menu=menubar)
    root.mainloop()
