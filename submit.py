#!/usr/bin/python

import cgi
import os
import shelve

print "Content-type: text/html\n\n"

form = cgi.FieldStorage()

if form.has_key('data'):
	data = form["data"].value
else:
	data = ""

if form.has_key('url'):
	url = form["url"].value
else:
	url = ""

user = os.environ["REMOTE_USER"]

print user, "is now working on", data

d = shelve.open("projects")

d[user] = (data, url)

d.close()
