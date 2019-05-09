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

class compactString:
    def __init__(self, orig_str):
        self.rep = myQueue()
        count = 0
        curr = ""
        for letter in orig_str:
            if curr == "":
                curr = letter
            if letter != curr:
                self.rep.add_last(((curr),count))
                curr = letter
                count = 1
            else:
                count +=1
        self.rep.add_last(((curr),count))
        
    def __str__(self):
        ans = ""
        cursor = self.rep.head
        while cursor != None:
            ans += cursor.value[0]*cursor.value[1]
            cursor = cursor.nextNode
        return ans
    
    def __add__(self, other):
        ans = compactString("")
        cursor = self.rep.head
        while cursor != None:
            ans.rep.add_last(cursor.value)
            cursor = cursor.nextNode
        cursor = other.rep.head
        while cursor != None:
            ans.rep.add_last(cursor.value)
            cursor = cursor.nextNode
        return ans

    def comp(self,other):
        #couldn't get this one to work
        return randint(-1,1)

        
    def __lt__(self,other):
        return self.comp(other)>0
    def __le__(self,other):
        return self.comp(other)>=0
    def __gt__(self,other):
        return self.comp(other)<0
    def __ge__(self,other):
        return self.comp(other)<=0
    def __repr__(self):
        return str(self)
            
                        

def test():
    bank = "abcdefg"
    for x in range(1000):
        control = ""
        for x in range(randint(0,10)):
            for y in range(randint(0,4)):
                control += bank[y]*x
        test = compactString(control)
        if(str(test) != str(control)):
            print(control,"\n",test)
            return False
        control2 = ""
        for x in range(randint(0,10)):
            for y in range(randint(0,4)):
                control2 += bank[y]*x
        test2 = compactString(control2)
        if(str(test+test2) != str(control+control2)):
            print(control+control2,"\n",test+test2)
            return False
        if((test < test2) != (control < control2)) or ((test <= test2) != (control <= control2)) or ((test > test2) != (control > control2)) or ((test >= test2) != (control >= control2)):
            print(control,"\n",control2,"\n",test.comp(test2))
            return False
    return True

