from random import randint
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if ind < 0:
            ind = len(self)+ind
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        return self.data[ind]


    def __setitem__(self, ind, val):
        if ind < 0:
            ind = len(self)+ind
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val

    def __str__(self):
        if self.n == 0:
            return "[]"
        ans = "["
        for x in range(self.n):
            ans+=str(self.data[x])+","
        return ans[0:-1]+"]"

    def __repr__(self):
        return str(self)

    def __add__(self,other):
        ans = MyList()
        ans.data =make_array(self.n+other.n)
        ans.n = self.n+other.n
        ans.capacity = ans.n
        for x in range(self.n):
            ans[x] = self.data[x]
        for x in range(other.n):
            ans[x+self.n] = other.data[x]
        return ans
    def __iadd__(self,other):
        for x in range(other.n):
            self.append(other.data[x])
        return self
    def __mul__(self,mulVal):
        ans = MyList()
        for x in range(mulVal):
            ans+=self
        return ans
    def __rmul__(self,other):
        return self * other
def testStr():
    print("\n\n\n\n\n\n testing str\n")
    newMyList = MyList()
    for x in range(20):
        print("current list: "+str(newMyList))
        newval = randint(-100,100)
        newMyList.append(newval)
        print("adding... " + str(newval))

def testRepr():
    print("\n\n\n\n\n\n testing repr\n")
    newMyList = MyList()
    for x in range(20):
        print("current list: ", end = "")
        print(newMyList)
        newval = randint(-100,100)
        newMyList.append(newval)
        print("adding... " + str(newval))
def testAdd():
    print("\n\n\n\n\n\n testing add\n")
    newMyList = MyList()
    newMyList2 = MyList()
    for x in range(10):
        print("current list1: "+str(newMyList))
        print("current list2: "+str(newMyList2))
        print("list1 + list2 = "+str(newMyList+newMyList2))
        newval = randint(-100,100)
        newval2 = randint(-100,100)
        newMyList.append(newval)
        newMyList2.append(newval2)
def testIadd():
    print("\n\n\n\n\n\n testing iadd\n")
    newMyList = MyList()
    newMyList2 = MyList()
    for x in range(10):
        print("current list1: "+str(newMyList))
        print("current list2: "+str(newMyList2))
        newMyList += newMyList2
        print("list1 + list2 = "+str(newMyList))
        newval = randint(-100,100)
        newval2 = randint(-100,100)
        newMyList.append(newval)
        newMyList2.append(newval2)

def testSetGet():
    newMyList = MyList()
    for x in range(10):
        newMyList.append(x)
    print(newMyList)    
    for i in range(len(newMyList)):
        print(newMyList[-1-i])
    for i in range(10,20):
        newMyList[9-i] = i
    print(newMyList)
def testMul():
    newMyList = MyList()
    for x in range(10):
        newMyList.append(x)
        print(newMyList * x)
def testRmul():
    newMyList = MyList()
    for x in range(10):
        newMyList.append(x)
        print(x* newMyList)
def reverse_string(input_str, low = 0, high = -1):
    if high == -1:
        high = len(input_str)-1
    if len(input_str) == 0:
        return ""
    if(low == high):
        return input_str[high]
    return input_str[high] + reverse_string(input_str,low,high-1)

def testReverse():
    test = "this is a test"
    print(reverse_string(test))
    test = "test????"
    print(reverse_string(test))
    test = ""
    print(reverse_string(test))
    test = "wow"
    print(reverse_string(test))
    test = "1234567"
    print(reverse_string(test))

testReverse()
#testRmul()
#testSetGet()                
#testAdd()
#testIadd()
#testMul()
