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
    
...
