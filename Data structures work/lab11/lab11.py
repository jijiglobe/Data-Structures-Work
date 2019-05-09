from random import randint
class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value
    
    # assumes key not in tree
    def subtree_insert_recursive(self, curr_root, key, value=None):
        if self.root == None:
            self.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
            self.size+=1
            return
        location = curr_root.item.key
        if key < location:
            if curr_root.left == None:
                self.size+=1
                curr_root.left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
            else:
                self.subtree_insert_recursive(curr_root.left,key,value)
        elif key > location:
            if curr_root.right == None:
                self.size+=1
                curr_root.right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
            else:
                self.subtree_insert_recursive(curr_root.right,key,value)

    def subtree_insert_iterative(self,key,value=None):
        if self.root == None:
            self.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
            self.size+=1
            return
        curr = self.root
        self.size+=1
        while True:
            if curr.item.key > key:
                if curr.left == None:
                    curr.left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
                    break
                else:
                    curr = curr.left
            if curr.item.key < key:
                if curr.right == None:
                    curr.right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(key, value))
                    break
                else:
                    curr = curr.right
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1
    
    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)
    
    def __str__(self):
        if self.root == None:
            return "[]"
        ans = "["
        for x in self.inorder():
            ans+=str(x.item.key)+", "
        return ans[0:-2]+"]"
     

def fca_bst(bst,node1,node2):
    less, more = node1, node2
    if node1.item.key > node2.item.key:
        less, more = more, less
    current = bst.root
    while not(current.item.key >= less.item.key and current.item.key<=more.item.key):
        if current.item.key > less.item.key:
            current = current.left
        else:
            current = current.right
    return current

def fca_bt(bt, node1, node2):
    ancestry = {}
    current = node1
    while current != bt.root:
        ancestry[current] = None
        current = current.parent
    current = node2
    while current not in ancestry:
        current = current.parent
    return current
        

def is_bst(bt):
    return bst_helper(bst.root)

def bst_helper(root):
    if root == None:
        return True
    if root.left != None and root.left.item.key > root.item.key:
        return False
    if root.right != None and root.right.item.key < root.item.key:
        return False
    return bst_helper(root.right) and bst_helper (root.left)
def test_insert():
    for x in range(10):
        control = BinarySearchTreeMap()
        recursive = BinarySearchTreeMap()
        iterative = BinarySearchTreeMap()
        keys = []
        for x in range(100):
            keys.append(x)
        for x in range(randint(0,15)):
            keyindex =randint(0,len(keys)-1)
            key = keys[keyindex]
            control.subtree_insert(key)
            recursive.subtree_insert_recursive(recursive.root,key)
            iterative.subtree_insert_iterative(key)
            del keys[keyindex]
        print("control  : ",control)
        print("recursive: ",recursive)
        print("iterative: ",iterative)
        print("")
test_insert()
def test_fca():
    pass

def test_is_bst():
    pass
    
