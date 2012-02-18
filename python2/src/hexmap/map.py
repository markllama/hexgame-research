# Describe a hex map
#
# 

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
    
    locations = relationship("Location", backref=backref("maps"))
    terrains = relationship("Terrain", backref=backref("maps"))
    tokens = relationship("Token", backref=backref("maps"))
    

    def __init__(self, name, size=Vector(15,22), origin=Vector()):

        self.name = name
        self.size = size
        self.origin = origin
