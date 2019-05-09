import copy
class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None

class myDequeue:
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

def permutations(lst):
    stack = []
    currentPerms = myDequeue()
    for x in lst:
        stack.append(x)
    currentPerms.add_first([stack.pop()])
    cursize = 2
    while len(stack) != 0:
        valueAdding = stack.pop()
        for y in range(len(currentPerms)):
            curperm = currentPerms.delete_first()
            for x in range(cursize+1):
                mycopy = copy.copy(curperm)
                mycopy.insert(x,valueAdding)
                currentPerms.add_last(mycopy)
    ans = []
    while not currentPerms.is_empty():
        ans.append(currentPerms.delete_first())
    return ans
