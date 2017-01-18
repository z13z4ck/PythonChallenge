f = open('3_character.txt','r')
import re
total = ""
# newchar = ''
for line in f:
	newchar = re.compile("(?<=[A-Z]{3})[a-z](?=[A-Z]{3})")
	# newchar = re.compile("[A-Z]{3}([a-z])[A-Z]{3}")
	val = newchar.match(line)
	# if val is not None:
	# print newchar.findall(line)
	total += "".join(newchar.findall(line))
print total
f.close()