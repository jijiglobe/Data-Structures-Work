from random import randint
class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None

class myQueue:
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
    def push(self, value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.head.prevNode = myNode(value)
            self.head.prevNode.nextNode = self.head
            self.head = self.head.prevNode
        self.size+=1
    def pop(self):
        self.size -=1
        stored = self.tail.value
        self.tail = self.tail.prevNode
        if self.tail != None:
            self.tail.next = None
        return stored
class Integer:
    def __init__(self, num_str):
        self.rep = myQueue()
        for x in num_str:
            self.rep.add_last(int(x))
    
    def __str__(self):
        cursor = self.rep.head
        ans = ""
        while cursor != None:
            ans+= str(cursor.value)
            cursor = cursor.nextNode
        return ans
    
    def __repr__(self):
        return str(self)

    def __add__(self, other):
        cursor1 = self.rep.tail
        cursor2 = other.rep.tail
        ans = Integer("")
        carry = 0
        while cursor1 != None or cursor2 != None:
            val1 = val2 = 0
            if cursor1 != None:
                val1 = cursor1.value
            if cursor2 != None:
                val2 = cursor2.value
            sumdigs = val1 + val2 + carry
            ans.rep.push(sumdigs%10)
            carry = sumdigs // 10
            if cursor1 != None:
                cursor1 = cursor1.prevNode
            if cursor2 != None:
                cursor2 = cursor2.prevNode
        if carry != 0:
            ans.rep.push(carry)
        return ans
            
def test():
    for x in range(100):
        val1 = randint(0,1000000)
        val2 = randint(0,1000000)
        test1 = Integer(str(val1))
        test2 = Integer(str(val2))
        if str(test1) != str(val1) or str(test2) != str(val2) or str(val1+val2) != str(test1+test2):
            print(val1,val2,val1+val2)
            print(test1,test2,test1+test2)
            return False
    return True

