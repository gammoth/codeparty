#!/usr/bin/python

print "Content-type: text/html\n\n"


content = open("list").readlines()



print open("header.html").read()

for x in content:
	print "<p> ", x, "</p>"


