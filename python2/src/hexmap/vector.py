#
# A location on a hex map
#

class Vector():

    def __init__(self, hx=0, hy=0):
        self.hx = hx
        self.hy = hy

    def __composite_values__(self):
        return self.hx, self.hy

    def __repr__(self):
        return "Vector(hx=%r, hy=%r)" % (self.hx, self.hy)

    def __eq__(self, other):
        return isinstance(other, Vector) and \
            other.hx == self.hx and \
            other.hy == self.hy

    def __ne__(self, other):
        return not self.__eq__(other)
