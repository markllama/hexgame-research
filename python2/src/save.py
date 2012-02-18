# Describe a hex map
#
# 

# 
# Create a common base class for declarative 
# 
from sqlalchemy.ext.declarative import declarative_base

SqlBase = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class Map(SqlBase):

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    terrains = relationship("Terrain", backref=backref("maps"))
    tokens = relationship("Token", backref=backref("maps"))

    def __init__(self, name):

        self.name = name


#
# Define a Hex Map Terrain
#

class Terrain(SqlBase):

    __tablename__ = "terrains"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    map_id = Column(Integer, ForeignKey("maps.id"))

    def __init__(self, name):
        
        self.name = name

    def __repr__(self):
        return "<Terrain name='%s'/>" % (self.name)


class Token(SqlBase):

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    map_id = Column(Integer, ForeignKey("maps.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Token name='%s'/>" % (self.name)
