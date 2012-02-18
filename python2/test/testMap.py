#!/usr/bin/python
#
# 
import unittest

from hexmap import SqlBase, Vector, Map, Terrain, Token

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestMap(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)

        SqlBase.metadata.create_all(self.engine)
    
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def testMap(self):

        m = Map("testMap")

        self.session.add(m)

        tmap = self.session.query(Map).first()

        self.assertEqual(m.name, tmap.name)
        self.assertEqual(m.size, Vector(15, 22))
        self.assertEqual(m.origin, Vector())

    def testAddTerrain(self):

        m = Map("testAddTerrain")
        self.session.add(m)
        
        t = Terrain("terrain")

        m.terrains.append(t)

        self.assertEqual(1, len(m.terrains))

    def testAddToken(self):

        m = Map("testAddToken")
        self.session.add(m)
        
        t = Token("token")

        m.tokens.append(t)

        self.assertEqual(1, len(m.tokens))

if __name__ == "__main__":


    unittest.main()

