import random
from MaxSubsequenceSumAndTimer import *
def move_zeroes(list):
    zeroes = 0
    for index in range(len(list)-1,-1,-1):
        list[index + zeroes] = list[index]
        if(list[index] == 0):
            zeroes+=1
            
    for x in range(zeroes):
        list[x] = 0
    return list

def reverse_vowels(string):
    vowels = "aeiou"
    string = list(string)
    vowelList = []
    locationList = []
    for index in range(len(string)):
        if(string[index] in vowels):
            vowelList.append(string[index])
            locationList.append(index)
    vowelList.reverse()
    for x in range(len(locationList)):
        string[locationList[x]] = vowelList[x]
    return "".join(string)

def generateRandomList(n):
    ans = []
    for x in range(n):
        ans.append(random.randint(-1000,1000))
    return ans

def testTimer():
    test1 = "N,V1,V2,V3\n"
    tests = []
    for x in range(7,13):
        tests.append(generateRandomList(2**x))
    for x in tests:
        timer = PolyTimer()
        maxSubsequenceSum1(x)
        time1 = timer.elapsed()
        timer.reset
        
        maxSubsequenceSum2(x)
        time2 = timer.elapsed()
        timer.reset

        maxSubsequenceSum3(x)
        time3 = timer.elapsed()
        timer.reset

        test1+=",".join([str(len(x)),str(time1),str(time2),str(time3)])+"\n"
    print(test1)

testTimer()   
#print(reverse_vowels("tandon"))
#print(move_zeroes([1,2,0,3,0,4,5]))
