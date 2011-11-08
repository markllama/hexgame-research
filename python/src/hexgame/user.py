#
# Hexgame user class and helpers
#
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

import hashlib

OrmBase = declarative_base()

class User(OrmBase):
    """
    A user of the hex game service
    """
    
    __tablename__ = "users"

    name = Column(String, primary_key=True)
    email = Column(String)
    hash = Column(String)

    def __init__(self, name, email, hash=None, password=None):
        self.name = name
        self.email = email
        # should be a hash
        if hash:
            self.hash = hash
        else:
            self.hash = hashlib.sha224(password).hexdigest()
    
    def repr(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.email, self.hash)


if __name__ == "__main__":
    db_filename = "test_user.sqlite3"
    













