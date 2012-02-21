# Describe a hex map
#
# 

from math import floor

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, composite

from sqlbase import SqlBase
from vector import Vector

class Map(SqlBase):

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    origin_hx = Column(Integer)
    origin_hy = Column(Integer)
    origin = composite(Vector, origin_hx, origin_hy)

    size_hx = Column(Integer)
    size_hy = Column(Integer)
    size = composite(Vector, size_hx, size_hy)
    
    locations = relationship("Location", backref=backref("map"))
    terrains = relationship("Terrain", backref=backref("map"))
    tokens = relationship("Token", backref=backref("map"))
    

    def __init__(self, name="unset", size=Vector(15,22), origin=Vector()):

        self.name = name
        self.size = size
        self.origin = origin


    def hxfirst(self):
        return self.origin.hx

    def hxcount(self):
        return self.size.hx


    def ybias(self, hx):
        return int(floor((hx - self.hxfirst()) / 2))


    def hyfirst(self, hx):
        first = self.hxfirst()
        if hx < first or hx >= first + self.hxcount():
            return None
        return self.origin.hy + self.ybias(hx)

    def hycount(self, hx):
        first = self.hxfirst();
        if hx < first or hx >= first + self.hxcount():
            return None;
        return self.size.hy;

    def contains(self, hv):
        normal = hv
        hxfirst = self.hxfirst();

        if normal.hx < hxfirst or normal.hx >= hxfirst + self.hxcount():
            return False

        hyfirst = self.hyfirst(normal.hx)
        if normal.hy < hyfirst or normal.hy >= hyfirst + self.hycount(normal.hx):
            return False

        return True


    def addTerrain(self, t):
        # check that t is a Terrain

        # check that t is not already present
        self.terrains.append(t)

    def addToken(self, t):
        # check that t is a Token

        # check that t is not already present
        self.tokens.append(t)

class TerrainList():
    """
    A list of terrains which can control what's added
    """


    def __getitem__(self, key):
        
        # check that the key is a Vector or Iterator

        # find the right 
        pass

    def __setitem__(self, key, value):
        pass
