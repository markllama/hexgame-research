# A Hex Map
"""
A hex map
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

from vector import Vector

class Map(object):
    __tablename__ = "maps"

 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(Vector)
    origin = Column(Vector)
    

    def __init__(self, *args, **kwargs)

name=None, size=Vector(15,22), origin=Vector.ORIGIN):
        id = 1
        self._name = name
        self._size = size
        self._origin = origin

    @property
    def name(self): return self._name

    @property
    def size(self): return self._size

    @property
    def origin(self): return self._origin
