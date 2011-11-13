#
# Hexgame user class and helpers
#
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

import hashlib
import uuid

import json
import lxml

from mimerender import mimerender

OrmBase = declarative_base()

class User(OrmBase):
    """
    A user of the hex game service
    """
    
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    hash = Column(String)

    def __init__(self, name, email, hash=None, password=None, id=None):
        self.name = name
        self.email = email
        # should be a hash
        if hash:
            self.hash = hash
        else:
            self.hash = hashlib.sha224(password).hexdigest()

        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())
    
    def repr(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.email, self.hash)

    def _render_html(**spec):        
        return html_template % (spec['name'], spec[email])

    _render_json = lambda(obj): json.dumps(obj)

    def _render_txt(**spec):
        return "User - Name: %s, Email: %s" % (spec[name], spec[email])

    @mimerender(
        default = "html",
        txt = _render_txt,
        html = _render_html,
        json = _render_json
        )
    def GET(self):
        return {"name": self.name, "email": self.email}

    html_template = """<user name="%s", email="%s"/>"""

    txt_template = """name: %s
email: %s
id: %s
"""


    













