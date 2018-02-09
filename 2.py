"""
    Python Challenge 02
    python source code to isolate normal character from a bunch of random ASCII character
"""
f = open('2_character.txt','r')
import re
newchar = ''
for line in f:
    # print line
    newchar += "".join(re.findall("[a-zA-Z]+",line))
print("Output = " + newchar)
f.close()




