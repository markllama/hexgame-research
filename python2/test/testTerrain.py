#!/usr/bin/python
#
# 
import unittest

from hexmap import Map, Terrain, Location, SqlBase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import time

class TestTerrain(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:', echo=True)

        SqlBase.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def testTerrain(self):

        t = Terrain("test")
        self.session.add(t)

        tnew = self.session.query(Terrain).first()

        self.assertEqual(t.name, tnew.name)


    def testAddLocation(self):

        m = Map("addLocationMap")
        self.session.add(m)
        t = Terrain("addLocationTerrain")
        m.terrains.append(t)

        l = Location(4, 5)
        m.locations.append(l)
        t.locations.append(l)

        print("location = %s", t.locations[0])



if __name__ == "__main__":
    unittest.main()

