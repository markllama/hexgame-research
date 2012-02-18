#
# Define a Hex Map Terrain
#

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from sqlbase import SqlBase

class Token(SqlBase):

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    map_id = Column(Integer, ForeignKey("maps.id"))

    location_id = Column(Integer, ForeignKey("locations.id"))
    location = relationship("Location", backref="tokens")
                             
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Token name='%s'/>" % (self.name)
