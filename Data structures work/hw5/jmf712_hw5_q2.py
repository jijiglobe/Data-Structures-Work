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

class midStack():
    def __init__(self):
        self.front = []
        self.back = myDequeue()
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def __len__(self):
        return self.size
    def top(self):
        return self.back.pop()
    def mid_push(self,value):
        if self.size == 0:
            self.front.append(value)
        elif self.size % 2 == 0:
            self.front.append(value)
        else:
            self.back.add_first(value)
        self.size +=1

    def push(self,value):
        if self.size == 0:
            self.front.append(value)
        elif self.size % 2 == 0:
            self.back.add_last(value)
            self.front.append(self.back.delete_first())
        else:
            self.back.add_last(value)
        self.size+=1

    def pop(self):
        if self.size % 2 == 1:
            self.back.add_first(self.front.pop())
        self.size -= 1
        return self.back.delete_last()
