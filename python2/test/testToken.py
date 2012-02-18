#!/usr/bin/python
#
# 
import unittest

from hexmap import SqlBase, Token

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestToken(unittest.TestCase):

    def testToken(self):

        engine = create_engine('sqlite:///:memory:', echo=True)

        SqlBase.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        t = Token("test")

        session.add(t)

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

