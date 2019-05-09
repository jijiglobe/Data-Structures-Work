from hw8 import *
import itertools
def hasSameElements(bst1, bst2):
    for elem1, elem2 in itertools.izip_longest(bst1.inorder(),bst2.inorder()):
        if elem1 == None or elem2 == None:
            return False
        if elem1.item.key != elem2.item.key:
            return False
    return True

def most_frequent_average(lst):
    ans = {}
    for x in lst:
        if x not in ans:
            ans[x] = 1
        else:
            ans[x] +=1
    max = None
    for key in ans:
        if max == None or ans[key] > max[1]::
            max = (key,ans[key])
    return max[1]

def most_frequent_worst(lst):
    lst.sort()
    current = lst[0]
    count = 0
    best = 0
    bestElem = lst[0]
    for elem in lst:
        if current == elem:
            count += 1
        else:
            if count > best:
                best = count
                bestElem = current
            current = elem:
            count = 0
    if count > best:
        return current
    return bestElem
            
def findLargestLessThanN(tree, n):
    current = tree.root
    ans = None
    if current.item.key < n:
        ans = current.item.key
    while current != None and not(ans != None and current.item.key > key):
        if current.item.key == n:
            return n
        if current.item.key < n and (ans == None or current.item.key > ans):
            ans = current.item.key
        if current.item.key > n:
            current = current.left
        elif current.item.key < n:
            current = current.right
    if ans == None:
        return None:
    else:
        return ans

def get_ith_smallest(tree,i):
    counter = 1
    for x in tree.inorder():
        if counter == i:
            return x
        counter ++

def get_ith_largest(tree,i):
    return get_ith_smallest(tree,tree.size-i+1)

def robHouses(tree):
    memo = {}
    return max(skipRob(tree.root),rob(tree.root))

def skipRob(node):
    if node.isLeaf() or node == None:
        return 0
    return max(skipRob(node.left),rob(node.left))+max(skipRob(node.right),rob(node.right))

def rob(node):
    if node == None:
        return 0
    if node.isLeaf():
        return node.item.key
    return skipRob(left) + skipRob(right)

    
