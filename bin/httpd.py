#!/usr/bin/python
#
# Copyright (C) 2010 Red Hat, Inc.
#
# This is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2.1 of
# the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this software; if not, write to the Free
# Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA, or see the FSF site: http://www.fsf.org.
#

#
# A simple test server to help test the REST client library behavior
#
# This uses the web.py library from http://webpy.org and starts from the 
# sample there.
#

import sys, os
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

from optparse import OptionParser, Option

import web
import json
from mimerender import mimerender

import pickle
import pprint

# Define user controllable defaults
defaults = {
    "webroot": "/home/mark/public_html",
}

for key in defaults:
    value = os.getenv(key.upper())
    if value is not None:
        defaults[key] = value

# Define normal control options for any script
standard_options = (
    Option("-d", "--debug", action="store_true"),
    Option("-n", "--dryrun", dest="liverun", action="store_false", default=True),
    Option("-v", "--verbose", action="store_true")
)

app_options = (
    Option(None, "--webroot", default=defaults['webroot']),
)

all_options = standard_options + app_options

# Create a list of url -> class mappings
# When a resource is requested, the corresponding object is created
# and then a method is called corresponding to the HTTP method used in the
# request.

# The HTTP method requests pass the HTTP request parameters as a dictionary
# to the class method.

class hello:        
    def GET(self, name=None):
        if not name: 
            name = 'World'
        return 'Hello, %s!\n' % name

class favicon:
    def GET(self, name=None):
        f = open(opt.webroot + "/favicon.ico")

class WebFile(object):

    def GET(self, name="/"):
        
        content = ""

        if name.endswith(".html"):
            web.header("Content-Type", "text/html")
        elif name.endswith(".js"):
            web.header("Content-Type", "application/javascript")
        elif name.endswith(".xml"):
            web.header("Content-Type", "text/xml")
                           
        # root = opt['webroot']
        fullname = opt.webroot + (name)
        print "looking for %s" % fullname

        if os.path.isfile(fullname):
            f = open(fullname)
            content = f.read()

        if os.path.isdir(fullname):
            web.header("Content-Type", "text/html")
            filelist = os.listdir(fullname)
            content = "<html>\n<body>\n<table border='2'>\n  <tr><td>" + ("</td></tr>\n  <td>".join(filelist)) + "</td></tr>\n</table>\n</body>\n</html>"



        return content

    def HEAD(self, name=None):
        web.header("X-Debug: %s" % name)
        return ""

"""
class RestApi(object):

    _resources = {
        "": Resource("", "application/xml", "<api>default</api>\n"),
        "initfile": Resource(
            "initfile", 
            "application/xml",
            "<text>This is the contents of the initial file</text>\n"
            ),
        }

    def _clear():
        logger = logging.getLogger(__name__ + ".clear")
        logger.debug("In the clear")
        RestApi._resources = {}

    def _load(filename):
        logger = logging.getLogger(__name__ + ".load")
        #filepath = opt.dataroot + filename
        filepath = "data/" + filename
        logger.info("Loading file %s" % filepath)

        #try:
        fd = open(filepath)

        if filepath.endswith(".py"):
            # import it
            RestApi._resources = eval(fd.read())
        else:
            # load it
            RestApi._resources = pickle.load(fd)

        fd.close()
        logger.info("data = %s" % RestApi._resources)

    def _save(filename):
        logger = logging.getLogger(__name__ + ".save")
        filepath = opt.dataroot + filename
        logger.debug("Saving file %s" % filepath)
        fd = open(filepath, "w")
        pickle.dump(RestApi._resources, fd)
        fd.close()

    actions = {'clear': (_clear, ()),
               'load': (_load, ('filename',)),
               'save': (_save, ('filename',))
               }

    def __init__(self, root=None):
        logger = logging.getLogger(self.__class__.__name__ + ".__init__")

        self.resources = RestApi._resources
        
    def GET(self, name):
        logger = logging.getLogger(self.__class__.__name__ + ".GET")

        logger.debug("my resources = %s" % self.resources)
        logger.debug("class resources = %s" % RestApi._resources)
        logger.debug("Searching for name '%s' in %s" % (name, self.resources.keys()))

        if name in self.resources:
            web.header("Content-Type", self.resources[name].mimetype)
            return self.resources[name].content
        else:
            raise web.notfound("resource %s does not exist\n" % name)
         
    def HEAD(self, name):
        logger = logging.getLogger(self.__class__.__name__ + ".HEAD")

        logger.debug("Searching for name %s in %s" % (name, self.resources.keys()))

        if name in self.resources:
            web.header("Content-Type", self.resources[name].mimetype)
            return ""

        else:
            raise web.notfound("resource %s does not exist\n" % name)

    def PUT(self, name):
        logger = logging.getLogger(self.__class__.__name__ + ".PUT")

        parent = os.path.dirname(name)

        if not parent in self.resources:
            raise web.forbidden("cannot create resource %s: Parent does not exist\n" % name)

        logger.debug("Put type: %s" % web.ctx.environ['CONTENT_TYPE'])

        # if it doesn't already exist, the return code is 201 Created
        created = name not in self.resources

        self.resources[name] = Resource(name, 
                                        web.ctx.environ['CONTENT_TYPE'],
                                        web.data())

        if created:
            raise web.created(name)

        web.header("Content-Type", "application/xml")
        return ""

    def DELETE(self, name):

        logger = logging.getLogger(self.__class__.__name__ + ".DELETE")

        if name == "":
            return web.forbidden("Cannot delete application root")

        if not name in self.resources:
            return web.notfound("no such resource: %s" % name)
        
        del(self.resources[name])

        web.header("Content-Type", "application/xml")
        return "<result status='success'/>\n"

    def POST(self, name):
        logger = logging.getLogger(self.__class__.__name__ + ".POST")
        web.header("Content-Type", "application/xml")
        
        if name in RestApi.actions:
            logger.debug("Executing action %s" % name)
            logger.debug("data = %s" % web.input())
            params = web.input()
            
            method = self.actions[name][0]
            kargs = {}
            for key in self.actions[name][1]:
                kargs[key] = params.get(key, None)
            
            method(**kargs)

        return "<result status='success'/>\n"

"""

urls = ("/hello", "hello", "/webfile(/.*)", "WebFile")

# Parse the command line argments
(opt, args) = OptionParser(option_list=all_options).parse_args()

# Push the remaining args back onto argv *AFTER* the call name (argv[0])
# web.application.run() uses argv for listener IP and port number
sys.argv[1:] = args

if __name__ == "__main__":
    logger = logging.getLogger("restserver")

    if opt.verbose:
        logging.root.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
        logger.info("user selected verbose output")
    if opt.debug:
        logging.root.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.debug("user select debugging output")
        
    app = web.application(urls, globals())
    app.run()
