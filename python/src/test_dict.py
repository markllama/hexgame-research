from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.collections import attribute_mapped_collection

SqlBase = declarative_base()

class Map(SqlBase):
    __tablename__ = 'map'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # proxy to 'user_keywords', instantiating UserKeyword
    # assigning the new key to 'special_key', values to
    # 'keyword'.
    terrains = association_proxy('map_terrains', 'terrain',
                                 creator=lambda k, v:
                                     UserKeyword(special_key=k, terrain=v)
                )

    def __init__(self, name):
        self.name = name

class UserKeyword(SqlBase):
    __tablename__ = 'user_keyword'
    user_id = Column(Integer, ForeignKey('map.id'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey('terrain.id'), primary_key=True)
    special_key = Column(String)

    # bidirectional user/user_keywords relationships, mapping
    # user_keywords with a dictionary against "special_key" as key.
    user = relationship(Map, backref=backref(
                    "map_terrains",
                    collection_class=attribute_mapped_collection("special_key"),
                    cascade="all, delete-orphan"
                    )
                )
    terrain = relationship("Terrain")

class Terrain(SqlBase):
    __tablename__ = 'terrain'
    id = Column(Integer, primary_key=True)
    keyword = Column('keyword', String(64))

    def __init__(self, keyword):
        self.keyword = keyword

    def __repr__(self):
        return 'Terrain(%s)' % repr(self.keyword)

if __name__ == "__main__":
    
    user = Map('log')

    user.terrains['sk1'] = Terrain('kw1')
    user.terrains['sk2'] = Terrain('kw2')

    print(user.terrains)
