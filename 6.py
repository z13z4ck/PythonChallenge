# solution for challenge 6
import re
f = open(r'channel\90052.txt','r')
print f.read()
line = f.readline(1)
f.close()
# line = "Next nothing is 94191"
# for line in f:
    # l = re.search
l = re.search("Next nothing is",line)
print l
