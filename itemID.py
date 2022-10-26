def convertToID(item):
    numStr = ""
    if(type(item)) == str:
        for i in item:
            numStr = numStr + str(ord(i)-23)
    return int(numStr)

def IDtoItem(ID):
    itemStr = ""
    if(type(ID)) == int:
        strID = str(ID)
        for i in range(int(len(strID)/2)):
            itemStr = itemStr + (chr(int(strID[2*i:(2*i)+2])+23))
    return itemStr