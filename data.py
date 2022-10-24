def getData():
    arr = {}
    data = open("data.txt", "r")
    lines = data.readlines()

    for textLine in lines:
        word = textLine.split(",")
        arr[word[0][0:len(word[0])]] = word[1][0:len(word[1])-1]
        #return data
    data.close()
    return arr

def addData():
    #add code here with user database
    return None

