from LinkedBinaryTree import *

def recreate_tree(preorder,inorder):
    ans = LinkedBinaryTree()
    ans.root = recHelper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    return ans

def recHelper(preorder,pfirst,plast,inorder,ifirst,ilast):
    if ifirst > ilast:
        return None #LinkedBinaryTree.Node(inorder[ifirst])
    if pfirst >= plast:
        if pfirst == plast:
            return LinkedBinaryTree.Node(preorder[ifirst])
        else:
            return None
    root = LinkedBinaryTree.Node(preorder[pfirst])
    inindex = inorder.index(root.data)
    root.left = recHelper(preorder,pfirst+1,pfirst+(inindex-ifirst)+1,inorder,ifirst,inindex-1)
    root.right = recHelper(preorder,pfirst+(inindex-ifirst)+1,plast,inorder,inindex+1,ilast)
    return root
    
def words_keep_numbers_flip(lst):
    nums = 0
    stack = []
    for index in range(len(lst)):
        lst[index-nums] = lst[index]
        if isinstance(lst[index],int):
            stack.append(lst[index])
            nums+=1
    for x in range(nums):
        lst.pop()
    while len(stack) >0:
        lst.append(stack.pop())

def testFlip():
    test = ["Keep", 3, "this","order",2,1]
    words_keep_numbers_flip(test)
    print(test)

def testDist():
    myTree = LinkedBinaryTree()
    testNodes = []
    for x in range(4):
        testNodes.append(LinkedBinaryTree.Node(0))
    node4 = LinkedBinaryTree.Node(0,testNodes[0],testNodes[1])
    node2 = LinkedBinaryTree.Node(0,node4)
    node3 = LinkedBinaryTree.Node(0,testNodes[2],testNodes[3])
    root = LinkedBinaryTree.Node(0,node2,node3)
    myTree.root = root
    print(myTree.subtree_children_dist(myTree.root))

class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None

class BoostQueue:
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
    def enqueue(self, value):
        if self.size == 0:
            self.head = self.tail = myNode(value)
        else:
            self.head.prevNode = myNode(value)
            self.head.prevNode.nextNode = self.head
            self.head = self.head.prevNode
        self.size+=1
    def boost(self,amount):
        if amount == 0:
            return
        holder = self.head.nextNode
        if self.size < amount:
            raise IndexError()
        if self.is_empty():
            raise IndexError()
        cursor = self.head
        for x in range(amount):
            cursor = cursor.nextNode
        self.head.nextNode.prevNode = None
        self.head.nextNode = cursor.nextNode
        cursor.nextNode = self.head
        self.head.prevNode = cursor
        self.head.nextNode.prevNode = self.head
        self.head = holder
    def dequeue(self):
        self.size -=1
        stored = self.tail.value
        self.tail = self.tail.prevNode
        if self.tail != None:
            self.tail.next = None
        return stored
    def __str__(self):
        ans = ""
        cursor = self.head
        while cursor != None:
            ans += str(cursor.value)+ " "
            cursor = cursor.nextNode
        return ans
    def __repr__(self):
        return str(self)

def testBoost():
    test = BoostQueue()
    for x in range(20):
        test.enqueue(x)
    for x in range(20):
        print(test)
        test.boost(x)

def testBoost():
    gen = recreate_tree("DBACEGF","ABCDEFG")
    ans = ""
    for x in gen.preorder():
        ans += x.data
    print("preorder: ",ans)
    ans = ""
    for x in gen.inorder():
        ans+=x.data
    print("postorder:",ans)

    gen = recreate_tree("BCAD","CBAD")
    ans = ""
    for x in gen.preorder():
        ans += x.data
    print("preorder: ",ans)
    ans = ""
    for x in gen.inorder():
        ans+=x.data
    print("postorder:",ans)
testBoost()
