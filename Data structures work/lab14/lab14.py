from random import randint
from LinkedBinaryTree import *
class PriorityQueue:
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None
    def __init__(self,head = None):
        self.head = head
    
    def push(self,key, value):
        newNode = PriorityQueue.Node(key,value)
        if self.head == None:
            self.head = newNode
        elif self.head.key > key:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next != None and current.next.key < key:
                current = current.next
            if current.next == None:
                current.next = newNode
            else:
                holder = current.next
                current.next = newNode
                newNode.next = holder
    def pop(self):
        if self.head == None:
            return None
        val = self.head.key
        self.head = self.head.next
        return val

class PriorityTree:
    def __init__(self):
        self.tree = LinkedBinaryTree()
        self.nextParent = None
    
    def push(self,data):
        if self.tree.root == None:
            self.tree.root = LinkedBinaryTree.Node(data)
            self.nextParent = self.tree.root
        else:
            if self.nextParent.left == None:
                self.nextParent.left = LinkedBinaryTree.Node(data)
                return
            else:
                self.nextParent.right = LinkedBinaryTree.Node(data)
                prev = self.nextParent
                current = self.nextParent.parent
                while current != None and prev != current.left:
                    prev = current
                    current = current.parent
                current = prev
                if current.right != None:
                    current = current.right
                    while current.left != None:
                        current = current.left
                self.nextParent = current
    
    def pop(self):
        ans = self.tree.root.data
        #print(self.tree.root.left)
        if self.tree.root.left == None:
            self.tree.root = None
            self.nextParent = None
            return ans
        if self.nextParent.left == None:
            prev = self.nextParent
            current = self.nextParent.parent
            while current != None and prev != current.right:
                prev = current
                current = current.parent
            if current == None:
                current = prev
            if current.left == None:
                self.nextParent = current
                return
            current = current.left
            
            while current.right != None:
                current = current.right
                nextParent = None
            self.nextParent = current.parent
            #nextParent Selected
            
            self.root.data = self.nextParent.right.data
            self.nextParent.right = None
            #deleted and swapped

            current = self.root
            while current != None:
                if (current.right == None or current.left.data < current.right.data) and current.left.data < current.data:
                    current.data, current.left.data = current.left.data, current.data
                    current = current.left
                elif current.right.data < current.left.data:
                    current.data, current.right.data = current.right.data, current.data
                    current = current.right
            #bubbledown complete

def test():
    control = []
    pqtest = []
    pq = PriorityQueue()
    pttest = []
    pt = PriorityTree()
    for x in range(randint(0,50)):
        newval = randint(0,100)
        print(newval, end = ",")
        control.append(newval)
        pq.push(newval,None)
        pt.push(newval)
    print()
    control.sort()
    for x in control:
        pqtest.append(pq.pop())
        pttest.append(pt.pop())
    print("control : ",control)
    print("priorityQ:",pqtest)
    print("Tree :    ",pttest)
test()
