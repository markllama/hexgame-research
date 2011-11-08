#!/usr/bin/python

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import unittest

from hexgame.user import User

db_filename = "unittest/data/testUser.sqlite3"

class TestUser(unittest.TestCase):

    def setUp(self):

        self.base = declarative_base()
        self.engine = create_engine('sqlite:///:memory:', echo=True)

        User.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()
        

    def tearDown(self):
        pass

    def testUser(self):
        
        u0 = User('testuser0', 'testuser0@example.com', password="notsecure0")
        u1 = User('testuser1', 'testuser1@example.com', password="notsecure1")
        u2 = User('testuser2', 'testuser2@example.com', password="notsecure2")

        self.session.add(u0)
        self.session.add(u1)
        self.session.add(u2)
        self.session.commit()

        u3 = self.session.query(User).filter_by(name="testuser1").first()

        self.assertEqual(u3.name, u1.name)


if __name__ == "__main__":
    unittest.main()
