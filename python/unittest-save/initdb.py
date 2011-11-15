#!/usr/bin/python
"""Initialize the test database"""

import sys

import sqlite3

if __name__ == "__main__":
    # check if the directory exists


    print "Creating database %s" % sys.argv[0]

    db = sqlite3.connect(sys.argv[1])

    # create the table of users
    
    db.execute("CREATE TABLE users(name text, email text, password text)")
    db.execute("""INSERT INTO users(name, email, password)
                 values ("user1", "user1@example.com", "notsecure1")""")
    db.execute("""INSERT INTO users(name, email, password)
                 values ("user2", "user2@example.com", "notsecure2")""")
    db.execute("""INSERT INTO users(name, email, password)
                 values ("user3", "user3@example.com", "notsecure3")""")
    db.commit()
    db.close()
