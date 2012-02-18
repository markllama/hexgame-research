#
#
#
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import composite, relationship

from sqlbase import SqlBase
from vector import Vector

class Location(SqlBase):

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    map_id = Column(Integer, ForeignKey("maps.id"))
    hx = Column(Integer)
    hy = Column(Integer)

    vector = composite(Vector, hx, hy)

    def __init__(self, hx, hy):
        self.hx = hx
        self.hy = hy


    def __repr__(self):
        return str(self.vector)
