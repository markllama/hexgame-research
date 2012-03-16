#!/usr/bin/python

# This is what we're going to build the application from
import web

# This will give the tools persistance
import sqlite3

# And this is the game proper
import hexgame

dbfile = "testdata.sqlite3"

# The list of query patterns
urls = (
    "/", "Landing"
)

class Landing:

    def GET(self):
        return "<html><head><title>Landing Page</title></head><body>Landing Page</body></html>"

if __name__ == "__main__":

    # connect to database
    db = sqlite3.connect(dbfile)

    app = web.application(urls, globals())
    app.run()

    db.close()
