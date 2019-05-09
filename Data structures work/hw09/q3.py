import random
#import UnsortedArrayMap as unsorted_map
class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None
class unsorted_map:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(unsorted_map.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.fifoList = myDLL()
        self.fifoPointers = {}
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if key not in self.fifoPointers:
            self.fifoList.add_last(key)
            self.fifoPointers[key] = self.fifoList.tail

        if self.table[j] is None:
            self.table[j] = unsorted_map()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        #delete from fifoshit
        current = self.fifoPointers[key]
        if current == self.fifoList.head:
            self.fifoList.delete_first()
        elif current == self.fifoList.tail:
            self.fifoList.delete_last()
        else:
            prev = current.prevNode
            next = current.nextNode
            prev.nextNode = next
            next.prevNode = prev
        #finished deleting
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        current = self.fifoList.head
        while current != None:
            yield current.value
            current = current.nextNode

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value


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

def test():
    test = ChainingHashTableMap()
    for x in range(100):
        test[x] = x
    for x in range(0,100,2):
        del test[x]
    for x in test:
        print(x)
#test()
