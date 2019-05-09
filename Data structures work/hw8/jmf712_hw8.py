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
            self.leftChildren = 0

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
        
        def isLeaf(self):
            return self.left == None and self.right == None

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
    
    def subtree_find_delete(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr.leftChildren -=1
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
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                self.root.leftChildren +=1
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr.leftChildren+=1
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                #parent.leftChildren +=1
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
        node_to_delete = self.subtree_find_delete(node, key)
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
                #node_to_delete.leftChildren -=1
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
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node

    def preorder(self, root=None):
        if root is None: root = self.root
        yield root
        if root.left is not None:
            for item in self.preorder(root.left):
                yield item
        if root.right is not None:
            for item in self.preorder(root.right):
                yield item
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

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)
    
    def get_ith_smallest(self,i):
        if i < 1 or i>self.size:
            raise IndexError()
        return self.get_ith_helper(self.root,i-1)
    
    def get_ith_helper(self,current, i):
        #print(current.item.key,current.leftChildren,i)
        if current.leftChildren == i:
            return current.item.key
        if current.leftChildren < i:
            return self.get_ith_helper(current.right,i-1-current.leftChildren)
        if current.leftChildren > i:
            return self.get_ith_helper(current.left,i)

def create_chain_bst(n):
    ans = BinarySearchTreeMap()
    for index in range(1,n+1):
        ans.subtree_insert(index)
    return ans

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst,start,finish):
    if start == finish:
        bst.subtree_insert(start)
    else:
        curr = (start+finish)//2
        bst.subtree_insert(curr)
        add_items(bst,start,curr-1)
        add_items(bst,curr+1,finish)

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    for key in prefix_lst:
        bst.subtree_insert(key)
    return bst

def find_min_abs_difference(bst):
    prev = None
    min = None
    for x in bst.inorder():
        if prev == None:
            prev = x.item.key
        elif min == None:
            min = x.item.key - prev
        elif x.item.key - prev < min:
            min = x.item.key - prev
        prev = x.item.key
    return min
            
def test():
    create_chain_bst(10)
    create_complete_bst(7)
    print(find_min_abs_difference(restore_bst([9,7,4,1,6,20,17,25])))
    for x in restore_bst([9,7,4,1,6,20,17,25]):
        print(x)
    print("\n\n\n")
    test = restore_bst([9,7,4,1,6,20,17,25])
    for x in range(1,len(test)+1):
        print(test.get_ith_smallest(x))
    print("\n\n\n\n")
    btest = BinarySearchTreeMap()
    for x in [7,5,1,14,10,3,9,13]:
        btest[x] = None
    print(btest.get_ith_smallest(3))
    print(btest.get_ith_smallest(6))
    del btest[14]
    del btest[5]
    print(btest.get_ith_smallest(3))
    print(btest.get_ith_smallest(6))

#test()
