from random import randint
from DoublyLinkedList import *
from LinkedBinaryTree import *

def flatten(nestedList):
    cursor = nestedList.header
    nexts = []
    ends = []
    while cursor != None:

        if isinstance(cursor.data,DoublyLinkedList):
            nexts.append(cursor.next)
            ends.append(cursor.data.trailer)
            if cursor.prev == None:
                cursor.data.header = nestedList.header
                cursor = cursor.data.header
            else:
                cursor.prev.next = cursor.data.header.next
                cursor.data.header.next.prev = cursor.prev
                cursor = cursor.prev
        else:
            ran = False
            while len(nexts) != 0 and (cursor.next == None or cursor.next.data == None):
                cursor.next = nexts.pop()
                cursor.next.prev = cursor
            if not ran and cursor != None:
                cursor = cursor.next
def generateRandomNestedList(limit):
    test = DoublyLinkedList()
    for x in range(randint(0,5)):
        if randint(0,3) == 0 and limit > 0:
            test.add_last(generateRandomNestedList(limit-1))
        else:
            test.add_last(randint(0,10))
    return test
def testFlatten():
    for x in range(100):
        test = generateRandomNestedList(4)
        print(test)
        flatten(test)
        print(test)
        print("\n\n\n")
def revereseTree(inputTree):
    frontier = [inputTree.root]
    while len(frontier) != 0:
        cursor = frontier.pop()
        cursor.left, cursor.right = cursor.right, cursor.left
        if cursor.left != None:
            frontier.append(cursor.left)
        if cursor.right != None:
            frontier.append(cursor.right)
def testReverse():
    pass

    
            
