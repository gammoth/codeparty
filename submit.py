#!/usr/bin/python

import cgi
import os

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

data = cgi.escape(form["data"].value)

user = os.environ["REMOTE_USER"]

print user, "is now working on", data

d = shelve.open("projects")

d['user'] = data

d.close()
