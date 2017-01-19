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

print l
integer =  int(filter(str.isdigit,l))
print str(integer)

print "next"

htmlurl1 = htmlurl + str(integer)
print htmlurl1

count = 1
while count < 400:
	print "Count = %d" %count
	html = Request(htmlurl+str(integer))
	print "Current HTML = %s" %(htmlurl + str(integer))
	htmlinfo = urllib2.urlopen(html)
	l = htmlinfo.read()
	if count == 85:
		integer = integer/2
		print "Dividing integer by 2"
	else:
		integer =  int(filter(str.isdigit,l))
	print "Current number = %d" %integer
	count+=1

