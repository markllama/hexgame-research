#!/usr/bin/python

import web

import hexgame

urls = (
    "/", "Landing"
)

class Landing:

    def GET(self):
        return "<html><head><title>Landing Page</title></head><body>Landing Page</body></html>"

if __name__ == "__main__":

    # connect to database

    app = web.application(urls, globals())
    app.run()
