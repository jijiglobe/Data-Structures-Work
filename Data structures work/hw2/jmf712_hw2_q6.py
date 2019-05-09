def two_sum(intList, target):
    for x in range(len(intList)):
        for y in range(len(intList)-1,x,-1):
            if intList[x] + intList[y] == target:
                return (x,y)
            if intList[x] + intList[y] < target:
                break
    return none
