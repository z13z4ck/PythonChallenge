import re
import urllib2
from urllib2 import urlopen
import pickle
url = "http://www.pythonchallenge.com/pc/def/banner.p"
html = urllib2.urlopen(url).read()
# print html
data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
print data
# data = str(data)
for line in data:
	print "".join([k*v for k,v in line])