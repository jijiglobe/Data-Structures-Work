def split_parity(intList):
    front = 0
    for index in range(len(intList)):
        if intList[index] % 2 == 1:
            intList[front], intList[index] = intList[index], intList[front]
            front+=1
    return intList

