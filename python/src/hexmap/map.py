# A Hex Map
"""
A hex map
"""

from math import floor

from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy import Column, Integer, String

from hexmap.sqlbase import SqlBase
from hexmap.vector import Vector
from hexmap.terrain import Terrain
from hexmap.token import Token

class Map(SqlBase):
    __tablename__ = "maps"

    _id = Column(Integer, primary_key=True)
    _name = Column(String)
    #_size = Column(Vector)
    #_origin = Column(Vector)

    terrains = relationship(
        'Terrain', 
        backref="map",
        collection_class=attribute_mapped_collection('name'),
        cascade="all, delete-orphan"
        )


    tokens = relationship(
        'Token', 
        backref="map",
        collection_class=attribute_mapped_collection('name'),
        cascade="all, delete-orphan"
        )
    
    # Map Constructor signatures
    # Map(String name)
    # Map(String name, Vector size)
    # Map(String name, Vector size, Vector origin)
    # Map(name=String, size=Vector, origin=Vector)

    def __init__(self, name="unset", size=Vector(15,22), origin=Vector.ORIGIN,
                 terrains=[], tokens=[]):

        assert(isinstance(name, str))
        self._name = name

        assert(isinstance(size, Vector))
        self._size = size

        assert(isinstance(origin, Vector))
        self._origin = origin

        assert(isinstance(terrains, list))
        for t in terrains:
            self.terrains[t.name] = t

        assert(isinstance(tokens, list))
        for t in tokens:
            self.tokens[t.name] = t

    @classmethod
    def fromElement(cls, element):
        pass

    @property
    def id(self): return self._id

    @property
    def name(self): return self._name

    @property
    def size(self): return self._size

    @property
    def origin(self): return self._origin

    def hxfirst(self):
        return self.origin.hx

    def hxcount(self):
        return self._size.hx


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
