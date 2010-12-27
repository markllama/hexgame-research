#!/usr/bin/python
"""Generate a triangular lattice in a rectangular frame"""

from Tkinter import *

import math

def sine60(a):
    return a * 8660 / 10000

hexrun = 15
hexradius = hexrun * 2
hexwidth = hexradius * 2
hexrise = sine60(hexradius)
hexheight = hexrise * 2

porigin = (200, 200)
horigin = (0, 0)

dim = {'hx': 14, 'hy': 22}

def vertices(px, py):
    return (px + hexradius, py,
            px + hexrun, py + hexrise,
            px - hexrun, py + hexrise,
            px - hexradius, py,
            px - hexrun, py - hexrise, 
            px + hexrun, py - hexrise,
            px + hexradius, py,
            )

def square(px, py):
    return(px, py, px + (hexrun * 3), py + hexheight)

def hex2point(hx, hy):
    px = (hx * hexrun * 3)
    py = (hy * hexheight) - ((hx * hexheight) / 2) 
    return (px, py)


def point2hex(px, py):
    # find the bounding hx columns
    hx = int((px - porigin[0]) / (hexrun * 3))
    hy = ((py - porigin[1]) + (hx * hexrise)) / hexheight

    # Technically, which ever hex center is closest to the point is the
    # right one.

    # Because of the nature of a triangular lattice on a cartesian plane
    # We can decide with a few specific rules.

    # normalize the pixel point location within the square
    qx = (px - porigin[0]) - (hx * (hexrun * 3))
    qy = (py - porigin[1]) - (hy * hexheight) + (hexrise * hx)
    print "p = (%d, %d), q = (%d, %d)" % (px, py, qx, qy)

    dl = (
        {'d2': qx**2 + qy**2, 'hex': (hx, hy)},
        {'d2': qx**2 + (hexheight - qy)**2, 'hex': (hx, hy+1)},
        {'d2': ((hexrun * 3) - qx)**2 + (qy - hexrise)**2, 'hex': (hx+1, hy+1)}
        )

    # return the hex who's center is nearest to the point passed in
    return min(dl, key=lambda a: a['d2'])['hex']
    
def pressedWhere(event):
    (hx, hy) = point2hex(event.x, event.y)
    print "You clicked on pixel(%d, %d).  Thats in hex(%d, %d)" % (event.x, event.y, hx, hy)



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
#        hexlist = self.rectangle(dim['hx'], dim['hy'])
        hexlist = self.hexagon(4, (250, 250))

        colors = ('yellow', 'blue', 'green', 'pink', 'brown', 'red', 'white')


        for hex in hexlist:
            p = hex['p']
            canvas.create_polygon(vertices(p[0], p[1]), outline='black', fill=colors[hex['hextant']])
#            canvas.create_rectangle(p[0]-1,p[1]-1,p[0]+1, p[1]+1)
#            canvas.create_line(vertices(p[0], p[1]))
            #canvas.create_rectangle(square(p[0], p[1]), dash=(2, 2))
            canvas.create_text(p[0], p[1], text=str(hex['h']))

            
    def rectangle(self, dim=(14,22), origin=(0,0)):
        result = []

        for col in range(0, dim[0]):
            ybias = int(col / 2)
            for row in range(ybias, dim[1] + ybias):
                p = hex2point(col, row)
                result.append({'h': (col, row), 
                               'p': (p[0] + origin[0], p[1] + origin[1])})
                print "creating node (%d, %d): %s" % (col, row, str(p))

        return result


    def hexagon(self, radius, origin=(0,0)):
        # create a full circle
        result = [{'h': (0, 0), 'p': (origin[0], origin[1]), 'hextant': 6}]
        for circle in range(1,radius+1):
            print "creating hexes with length " + str(circle)
       

            for hex in range(0, circle):
                hx = hex
                hy = -circle + hex 
                hz = -circle

                hexloop = (hx, hy, hz, -hx, -hy, -hz, hx)
                for hextant in range(0,6):
                    h = (hexloop[hextant], hexloop[hextant+1])
                    p = hex2point(hexloop[hextant], hexloop[hextant+1])
                    print "creating node (%d, %d): %s" % (hexloop[hextant],
                                                          hexloop[hextant+1],
                                                          str(p))
                
                    result.append({'h': h, 
                                   'p': (p[0] + origin[0], p[1] + origin[1]),
                                   'hextant': hextant
                                   })


        return result

if __name__ == "__main__":

    root = Tk()
    root.title('Tri Lattace')
    root.geometry("500x500")

#    menubar = MenuBar(root)
#    menubar.pack(side=TOP)
    map = TriMap(root)
    map.pack(fill=BOTH, expand=1)
#    root.config(menu=menubar)
    root.mainloop()
