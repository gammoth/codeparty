#!/usr/bin/python

import shelve

print "Content-type: text/html;charset=utf-8\n\n"

print open("header.html").read()

c = shelve.open("projects")

print "<ul>"
for x in c:
	print "<li>", x,": ", c[x][0], "<a href=\"", c[x][1], "\">", c[x][1],  "</a></li>"

print "</ul>"

print open("footer.html").read()

