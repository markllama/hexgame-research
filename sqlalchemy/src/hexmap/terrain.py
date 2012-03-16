#
# A single terrain
#

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

from hexmap.sqlbase import SqlBase

class Terrain(SqlBase):
    """
    a hex modifier
    """

    __tablename__ = 'terrains'

    _id = Column(Integer, primary_key=True)
    _name = Column(String)
    _map = Column(Integer, ForeignKey('maps._id'))

    def __init__(self, name, map=None, locations=[]):
        self._name = name
        self._map = map
        self._locations = locations

    @property
    def name(self): return self._name

    @property
    def map(self): return self._map

    @map.setter
    def map(self, newmap): self._map = newmap

    @property
    def name(self): return self._name

    @property
    def locations(self): return self._locations


