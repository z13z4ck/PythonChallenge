# solution for challenge 6
import re
f = open(r'channel\90052.txt','r')
print f.read()
line = f.readline()
f.close()
# line = "Next nothing is 94191"
# for line in f:
	# l = re.search
l = re.match("nothing is (\d+)",line)
print l.group(1)
