#the final is 250

import urllib2
from urllib2 import Request
htmlurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

# from urllib2 import Request
import re
html = Request("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
htmlinfo = urllib2.urlopen(html)

# htmldata = re.findall("<body>(.*?)</body>",htmlinfo.read(),re.DOTALL)[-1]
# print htmlinfo.read()
l = htmlinfo.read()

#read in another 	
l = re.search("next nothing is (\d+)", l)

print l.group(0)
print "test %s"%l.group(1)
print htmlurl + l.group(1)

new  = htmlurl + l.group(1)

# Request(htmlurl + l.group(1))

integer = l.group(1)
# integer =  int(filter(str.isdigit,l))
# print str(integer)

# print "next"

# htmlurl1 = htmlurl + str(integer)
# print htmlurl1

count = 1
while count < 400:
	print "Count = %d" %count
	new = htmlurl + str(integer)
	html = Request(new)
	htmlinfo = urllib2.urlopen(html)
	print "Current HTML = %s" %(new)
	
	htmlinfo = urllib2.urlopen(html)
	l = htmlinfo.read()
	l = re.search("next nothing is (\d+)", l)
	if count == 85:
		integer = integer/2
		print "Dividing integer by 2"
	else:
		integer =  int(l.group(1))
	print "Current number = %d" %integer
	count+=1

