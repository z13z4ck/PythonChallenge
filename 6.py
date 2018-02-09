# solution for challenge 6
import re,zipfile
f = open(r'channel\90052.txt','r')
print(f.read())
line = f.read()
f.close()
# line = "Next nothing is 94191"
# for line in f:
    # l = re.search
l = re.search("Next nothing is (\D+)",line)
print (l)

comments=[]



# simple and better
print("2nd try")
f = zipfile.ZipFile("channel.zip")

currentnum = 90052
while True:
    content = f.read(str(currentnum) + '.txt').decode('utf-8')
    print (content)
    comments.append(f.getinfo(str(currentnum)+'.txt').comment.decode('utf-8'))
    match = re.search("Next nothing is (\d+)",content)
    try:
        currentnum = match.group(1)
    except Exception:
        print("".join(comments))
        break
