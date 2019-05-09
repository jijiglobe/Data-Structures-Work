from random import randint
def maximum(lst, index=0, max=None):
    if len(lst)==0:
        return None
    if len(lst) == 1:
        return lst[index]
    if max == None:
        max = lst[index]
    if lst[index] > max:
        max = lst[index]
    if index == len(lst)-1:
        return max
    return maximum(lst,index+1,max)

def test_max():
    test_passed = True
    for x in range(200):
        test = []
        for y in range(randint(1,50)):
            test.append(randint(-100,100))
        if max(test) != maximum(test):
            print(test)
            print(maximum(test))
            print(max(test))
            test_passed = False
    print(test_passed)

def summate(lst):
    ans = 0
    for elem in lst:
        if isinstance(elem,int):
            ans += elem
        if isinstance(elem,list):
            ans+= summate(elem)
    return ans

def test_sum():
    test = [[1,2],[3,[[4],5]],6,[]]
    print(test)
    print(summate(test))
    test = [[1,2],[3,[[4],5]],6,[],2,4]
    print(test)
    print(summate(test))
    test = [1,2,4,5]
    print(test)
    print(summate(test))
    test = [[],[],[],[]]
    print(test)
    print(summate(test))
    test = [[1,2,3,[3],[4,[5]]]]
    print(test)
    print(summate(test))

def roll_the_dice(n):
    ans = []
    for x in range(n):
        ans.append(str(randint(1,6)))
    return " ".join(ans)

def testDice():
    for x in range(30):
        print(roll_the_dice(randint(0,30)))

def intersect(lst1,lst2):
    index1 = index2 = 0
    ans = []
    seen = set()
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] == lst2[index2]:
            if lst1[index1] not in seen:
                ans.append(lst1[index1])
                seen.add(lst1[index1])
                index1+=1
                index2+=1
            else:
                index1+=1
                index2+=1
        elif lst1[index1] < lst2[index2]:
            index1+=1
        elif lst1[index1] > lst2[index2]:
            index2 +=1
    return ans

def testInter():
    test1 = [1,6,14,15]
    test2 = [2,6,14,19]
    test1.sort()
    test2.sort()
    print("Test 1: " ,test1)
    print("Test 2: " ,test2)
    print("inters: " ,intersect(test1,test2))

    test1 = [1,6,14,15]
    test2 = [5,5,5,5,5]
    test1.sort()
    test2.sort()
    print("Test 1: ",test1)
    print("Test 2: ",test2)
    print("inters: ",intersect(test1,test2))

    test1 = [1,6,14,15]
    test2 = [1,6,14,15]
    test1.sort()
    test2.sort()

    print("Test 1: " ,test1)
    print("Test 2: " ,test2)
    print("inters: " ,intersect(test1,test2))

    test1 = [1,3,5,6,2,4,6,1]
    test2 = [1,2,56,1,4,1,2,3,4]
    test1.sort()
    test2.sort()

    print("Test 1: " ,test1)
    print("Test 2: " ,test2)
    print("inters: " ,intersect(test1,test2))

def winGame(lst, index = 0):
    if index == len(lst)-1:
        return True
    solved = False
    for x in range(1,lst[index]+1):
        if winGame(lst,index+x):
            solved = True
            break
    return solved

def testGame():
    test = [3,3,1,0,2,0,1]
    print(test)
    print(winGame(test))
    test = [3,2,0,0,2,0,1]
    print(test)
    print(winGame(test))
    test = [0]
    print(test)
    print(winGame(test))
    test = [0,0,0,0,0]
    print(test)
    print(winGame(test))
    test = [1,1,1,1,1,1,1]
    print(test)
    print(winGame(test))
    test = [3,2,1,0]
    print(test)
    print(winGame(test))

