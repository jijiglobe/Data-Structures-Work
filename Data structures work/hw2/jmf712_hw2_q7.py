def findChange(binList):
    bottom = 0
    top = len(binList) - 1
    index = int(top/2)
    while not( binList[index-1] == 0 and binList[index] == 1):
        if(binList[index] == 1):
            top = index
            index = int((top + bottom)/2)
        else:
            bottom = index
            index = int((top + bottom)/2)+1
    return index
