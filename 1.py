character = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."	 
newchar = ''
print(character)

for i in range(0,len(character)):
    # print character[i]
    # print ord(character[i])
    if (ord(character[i]) != 32):
        if (ord(character[i]) != 46):
            if (ord(character[i])> 120):
                newchar += chr(ord(character[i])-120+96)
            else:
                newchar += chr(ord(character[i]) + 2)
        else:
            newchar += chr(ord(character[i]))
    else:
        newchar += chr(ord(character[i]))


print(newchar)