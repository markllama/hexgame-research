#!/usr/bin/python
"""
Hex game server
"""

import web
from mimerender import mimerender
import json
import lxml

render_json = lambda **args: json.dumps(args)

class Landing:
    """
    This is the landing page for the hex game service.
    It returns a page or an object containing links to the resources needed
    to play the game
    """

    def _render_html(**links):

        response = """<html>
  <head>
    <title>Hex Game</title>
    <style>
      
    </style>
  </head>
  <body>
    <!-- header -->
    <div id="header"
      <h1>Hex Game Home</h1>
      <p>
        Welcome to the Hex Game Home
      </p>
    </div>
    <!-- links -->
    <div id="roadmap">
      <ul>
        <li><a href="%s">Register</a></li>
        <li><a href="%s">Users</a></li>
        <li><a href="%s">Games</a></li>
        <li><a href="%s">Matches</a></li>
      </ul>
    </div>
    <!-- footer -->
  </body>
</html>
"""
        
        return response % (
            links['register'], 
            links['users'], 
            links['games'], 
            links['matches']
            )
                           

    @mimerender(
        default="html", 
        html = _render_html,
        #xml = _render_xml,
        json = render_json
        )
    def GET(self):
        links = {
            "register": "/register",
            "users": "/users",
            "games": "/games",
            "matches": "/matches"
            }
        return links

class Register:
    """
    The registration form for new Hex Game users
    
    For HTML provide the form and a submit link to begin registration.

    For others, provide user object template and a reference to the
    users container.  A REST client can POST a completed instance of the
    object for insertion.

    This might be done by merely redirecting to the users container
    """

    
    pass

class Users:
    """
    The collection of users of the who have registered to play games
    """

    users = []

    def _render_html(users):
        template = """<html>
  <head>
    <title>Hex Game Users</title>
  </head>
  <body>
    <div id="header">
    </div>
    <div id="users">
      Hex Game User List
      <ul id="userlist">
       %s
      </ul>
    </div>
  </body>
</html>
"""

        user_strings = []
        for user in users:
            user_strings.append('<li><a href="">%s</a></li>' % user.name)

        return template % "\n".join(user_strings)

    @mimerender(
        default = 'html',
        html = _render_html,
        #xml = _render_xml,
        json = render_json
        )
    def GET(self):
        # don't return the password
        list = [{'name': u.user, 'email': u.email} for u in self.users]
        return {'users': list}

        
class User:
    """
    A single account for a person who plays hex games
    
    """

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        # this should be hashed
        self.password = password


    def to_html(self):
        pass

    def to_xml(self):
        pass

    def to_json(self):
        pass

    def template():
        pass

urls = (
    '/', 'Landing',
    '/register', 'Register',
    '/users', 'Users'
)
app = web.application(urls, globals())

users = [
    User('testuser1', 'testuser1@example.com', 'notsecure1'),
    User('testuser2', 'testuser2@example.com', 'notsecure2'),
    User('testuser3', 'testuser3@example.com', 'notsecure3'),
    User('testuser4', 'testuser4@example.com', 'notsecure4'),
    User('testuser5', 'testuser5@example.com', 'notsecure5'),
]

if __name__ == "__main__":

    
    app.run()
