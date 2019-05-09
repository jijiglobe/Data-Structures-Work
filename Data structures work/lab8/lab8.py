from random import randint
class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None
class myStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def last(self):
        return self.tail

    def push(self,value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.tail.nextNode = myNode(value)
            self.tail.nextNode.prevNode = self.tail
            self.tail = self.tail.nextNode
        self.size+=1

    def pop(self):
        self.size -=1
        stored = self.tail.value
        self.tail = self.tail.prevNode
        if self.tail != None:
            self.tail.next = None
        return stored
def testStack():
    failed = False
    for x in range(100):
        mine = myStack()
        pythons = []
        sizeof = randint(0,100)
        for x in range(sizeof):
            val = randint(0,10)
            mine.push(val)
            pythons.append(val)
        for x in range(sizeof):
            myval = mine.pop()
            pyval = pythons.pop()
            print("myval: ", myval)
            print("python:", pyval)
            if myval !=pyval:
                failed = True
    print(failed)

class myLeakyStack:
    def __init__(self,maxSize):
        self.head = None
        self.tail = None
        self.size = 0
        self.maxSize = maxSize

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def last(self):
        return self.tail

    def push(self,value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.tail.nextNode = myNode(value)
            self.tail.nextNode.prevNode = self.tail
            self.tail = self.tail.nextNode
        self.size+=1
        if self.size > self.maxSize:
            self.size -=1
            self.head = self.head.nextNode
            if self.head != None:
                self.head.prevNode = None

    def pop(self):
        self.size -=1
        stored = self.tail.value
        self.tail = self.tail.prevNode
        if self.tail != None:
            self.tail.next = None
        return stored
def testLeaky():
    test = myLeakyStack(5)
    test.push(2)
    test.push(13)
    test.push(3)
    test.push(8)
    test.push(5)
    test.push(12)
    while not test.is_empty():
        print(test.pop())
    failed = False
    print("wait...")
    waiting = input()
    for x in range(100):
        mine = myStack()
        pythons = []
        sizeof = randint(0,100)
        for x in range(sizeof):
            val = randint(0,10)
            mine.push(val)
            pythons.append(val)
        for x in range(sizeof):
            myval = mine.pop()
            pyval = pythons.pop()
            print("myval: ", myval)
            print("python:", pyval)
            if myval !=pyval:
                failed = True
    print(failed)
    

class myDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def first(self):
        return self.head
    def last(self):
        return self.tail
    def add_first(self, value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.head.prevNode = myNode(value)
            self.head.prevNode.nextNode = self.head
            self.head = self.head.prevNode
        self.size+=1
    def add_last(self,value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.tail.nextNode = myNode(value)
            self.tail.nextNode.prevNode = self.tail
            self.tail = self.tail.nextNode
        self.size+=1
    def __str__(self):
        if self.size == 0:
            return "[]"
        ans = "["
        cursor = self.head
        while cursor != None:
            ans+=str(cursor.value) + ", "
            cursor = cursor.nextNode
        ans = ans[:-2]+"]"
        return ans
    def reverse_list1(self):
        front = self.head
        back = self.tail
        for x in range(self.size//2):
            front.value , back.value = back.value, front.value
            front = front.nextNode
            back = back.prevNode
    def reverse_list2(self):
        if self.size == 0:
            return
        cursor = self.head
        while cursor != None:
            cursor.nextNode, cursor.prevNode = cursor.prevNode, cursor.nextNode
            cursor = cursor.prevNode
        self.head, self.tail = self.tail, self.head
            
    def delete_first(self):
        self.size -=1
        stored = self.head.value
        self.head = self.head.nextNode
        if self.head != None:
            self.head.prevNode = None
        return stored
    def delete_last(self):
        self.size -=1
        stored = self.tail.value
        self.tail = self.tail.prevNode
        if self.tail != None:
            self.tail.next = None
        return stored

def testReverse():
    for x in range(100):
        control = []
        test1 = myDLL()
        test2 = myDLL()
        for x in range(randint(0,20)):
            val = randint(0,10)
            control.append(val)
            test1.add_last(val)
            test2.add_last(val)
        print("control: ", control)
        control = control[::-1]
        test1.reverse_list1()
        test2.reverse_list2()

        print("control: ", control)
        print("test1:   ", test1)
        print("test2:   ", test2)

