#
# Define a Hex Map Terrain
#

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from sqlbase import SqlBase

terrain_locations = Table(
    "association", SqlBase.metadata,
    Column('terrain_id', Integer, ForeignKey('terrains.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
    )

class Terrain(SqlBase):

    __tablename__ = "terrains"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    map_id = Column(Integer, ForeignKey("maps.id"))

    locations = relationship("Location",
                             secondary=terrain_locations,
                             backref="terrains")

    def __init__(self, name):
        
        self.name = name

    def __repr__(self):
        return "<Terrain name='%s'/>" % (self.name)
