class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class EmptyCollection(Exception):
    pass


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1


    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if(subtree_root is None):
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)


    def __iter__(self):
        for node in self.inorder():
            yield node.data


    def breadth_first(self):
        if(self.is_empty()):
            return
        nodes_q = ArrayQueue()
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty() == False):
            curr_node = nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if (curr_node.right is not None):
                nodes_q.enqueue(curr_node.right)
    
    def subtree_children_dist(self,curr_root):
        if curr_root.left == None and curr_root.right == None:
            return [1,0,0]
        ans = [0,0,0]
        if (curr_root.left == None and curr_root.right != None) or (curr_root.left != None and curr_root.right == None):
            ans[1] +=1
        if curr_root.left != None and curr_root.right != None:
            ans[2] +=1
        if curr_root.left != None:
            additive = self.subtree_children_dist(curr_root.left)
            ans[0] += additive[0]
            ans[1] += additive[1]
            ans[2] += additive[2]
        if curr_root.right != None:
            additive = self.subtree_children_dist(curr_root.right)
            ans[0] += additive[0]
            ans[1] += additive[1]
            ans[2] += additive[2]
        return ans

    def leaves_list(self):
        if self.root == None:
            return []
        frontier = []
        leaves = []
        frontier.append(self.root)
        while len(frontier) != 0:
            currentNode = frontier.pop()
            if currentNode.left == None and currentNode.right == None:
                leaves.append(currentNode.data)
            if currentNode.right != None:
                frontier.append(currentNode.right)
            if currentNode.left != None:
                frontier.append(currentNode.left)
        return leaves

    def iterative_inorder(self):
        current = self.root
        while current != None:
            if current.left == None:
                yield current.data
                current = current.right
            else:
                pred = current
                while pred.right != None:
                    pred = pred.right
                pred.right = current
                current = current.left

def create_expression_tree(prefix_exp_str):
    exp = " ".split(prefix_exp_str)
    ans = LinkedBinaryTree()
    ans.root = expression_helper(exp,0)[0]
    return ans
def expression_helper(exp_list,start):
    valids = ["+","/","*","-"]
    root = LinkedBinaryTree.Node(exp_list[start])
    if root.data not in valids or start >= len(exp_list):
        return (root,1)
    left = expression_helper(exp_list,start+1)
    right = expression_helper(exp_list,start+left[1])
    size = left[1] + right[1]
    root.left = left
    root.right = right
    return (root,size)

def is_height_balanced(bin_tree):
    return balance_helper(bin_tree.root)[0]

def balance_helper(root):
    if root == None:
        return (True, 0)
    left = balance_helper(root.left)
    right = balance_helper(root.right)
    if left[0] == False or right[0] == False:
        return (False,0)
    diff = left[1] - right[1]
    if diff <-1 or diff > 1:
        return (False,0)
    return (True, max(left[1],right[1])+1)

def min_and_max(bin_tree):
    if bin_tree.root == None:
        raise Exception("EmptyTree")
    return subtree_min_and_max(bin_tree, bin_tree.root)

def subtree_min_and_max(bin_tree, subtree_root):
    if subtree_root == None:
        return None
    left = subtree_min_and_max(bin_tree, subtree_root.left)
    right = subtree_min_and_max(bin_tree, subtree_root.right)
    if left == None and right == None:
        return (subtree_root.data,subtree_root.data)
    if left == None:
        return (min(subtree_root.data,right[0]),max(subtree_root.data,right[1]))
    if right == None:
        return (min(subtree_root.data,left[0]),max(subtree_root.data,left[1]))
    return (min(subtree_root.data,left[0],right[0]),max(subtree_root.data,left[1],right[1]))
