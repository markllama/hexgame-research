#!/usr/bin/python
#
# Test SQLAlchemy
#
import time


from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()

class Map(Base):

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return  "<Map name='%s'/>" % (self.name)

if __name__ == "__main__":
    engine = create_engine('sqlite:///:memory:', echo=True)

    Session.configure(bind=engine)

    session = Session()
    
    Base.metadata.create_all(engine)

    m = Map("test")

    session.add(m)

    session.commit()

    time.sleep(10)

    session.close()


    

