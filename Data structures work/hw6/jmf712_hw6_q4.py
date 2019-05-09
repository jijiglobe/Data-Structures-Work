from random import randint
class EmptyCollection(Exception):
    pass


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

def copy_linked_list(lnk_lst):
    cursor = lnk_lst.header.next
    ans = DoublyLinkedList()
    while cursor != lnk_lst.trailer:
        ans.add_last(cursor.data)
        cursor = cursor.next
    return ans

def deep_copy_linked_list(lnk_lst):
    ans = DoublyLinkedList()
    cursor = lnk_lst.header.next
    while cursor !=lnk_lst.trailer:
        if isinstance(cursor.data,DoublyLinkedList):
            ans.add_last(deep_copy_linked_list(cursor.data))
        else:
            ans.add_last(cursor.data)
        cursor = cursor.next
    return ans
def generateRandomNestedList(limit):
    test = DoublyLinkedList()
    for x in range(randint(0,5)):
        if randint(0,3) == 0 and limit > 0:
            test.add_last(generateRandomNestedList(limit-1))
        else:
            test.add_last(randint(0,10))
    return test
def checkShallow(lst1,lst2):
    cursor1 = lst1.header.next
    cursor2 = lst2.header.next
    while cursor1 != lst1.trailer:
        if cursor1.data != cursor2.data:
            return False
        cursor1 = cursor1.next
        cursor2 = cursor2.next
    return True
def test():
    for x in range(10):
        orig = generateRandomNestedList(4)
        shallow = copy_linked_list(orig)
        deep = deep_copy_linked_list(orig)
        print(orig)
        print(shallow)
        print(deep)
        print(checkShallow(orig,shallow) and (not checkShallow(orig,deep)))
        print("\n")
