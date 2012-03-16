#
# A single token
#

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from hexmap.sqlbase import SqlBase

class Token(SqlBase):
    """
    Hex Contents
    """
    __tablename__ = "tokens"

    _id = Column(Integer, primary_key=True)
    _name = Column(String, unique=True, nullable=False, index=True)
    _map = Column(Integer, ForeignKey('maps._id'))

    def __init__(self, name, map=None, location=None):
        self._name = name
        self._map = map
        self._location = location

    @property
    def name(self): return self._name

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def name(self): return self._name

    @property
    def location(self): return self._location


