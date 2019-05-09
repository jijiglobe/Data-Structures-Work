from StackAndQueue import *
def balanced_expression(input):
    myStack = ArrayStack()
    for x in input:
        if x in "{[(":
            myStack.push(x)
        if x in "]})":
            if myStack.is_empty():
                return False
            topval = myStack.pop()
            if x == "]" and topval != "[":
                return False
            if x == "}" and topval != "{":
                return False
            if x == ")" and topval != "(":
                return False
    if myStack.is_empty():
        return True
    return False

class myNode:
    def __init__(self, value):
        self.value = value
        self.prevNode = None
        self.nextNode = None

class myDequeue:
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
def testDequeue():
    print("\n\nadding first, subtracting first")
    deq1 = myDequeue()
    for x in range(10):
        deq1.add_first(x)
    while len(deq1) >0:
        print(deq1.delete_first())
    print("\n\nadding last, subtracting first")
    deq1 = myDequeue()
    for x in range(10):
        deq1.add_last(x)
    while len(deq1) >0:
        print(deq1.delete_first())
    print("\n\nadding first, subtracting last")
    deq1 = myDequeue()
    for x in range(10):
        deq1.add_first(x)
    while len(deq1) >0:
        print(deq1.delete_last())
    print("\n\nadding last, subtracting last")
    deq1 = myDequeue()
    for x in range(10):
        deq1.add_last(x)
    while len(deq1) >0:
        print(deq1.delete_last())

def test_balance():
    testcase = "(({{[]}})"
    print(testcase)
    print(balanced_expression(testcase))
    testcase = "(({{[]}}))"
    print(testcase)
    print(balanced_expression(testcase))
    testcase = "(({{[]}})))"
    print(testcase)
    print(balanced_expression(testcase))
    testcase = "([]{{[]}()})"
    print(testcase)
    print(balanced_expression(testcase))

def printMaze(maze):
    print("\033c")
    for row in maze:
        for item in row:
            print(item, " ", end="")
        print()

class space:
    def __init__(self,location,prev):
        self.location = location
        self.prev = prev
def retrace(maze, current):
    steps = 1
    current = current.prev
    while current.prev != None:
        maze[current.location[0]][current.location[1]] = "#"
        current = current.prev
        steps+=1
    printMaze(maze)
    print("It took",steps,"steps to complete the maze.")

def mazeSolver():
    temp_file = open("maze.txt")
    lines = temp_file.readlines()
    temp_file.close
    maze = []
    for item in lines:
        maze.append(item.split())
    printMaze(maze)
    visited = {}
    frontier = ArrayStack()
    frontier.push(space((1,1),None))
    while not frontier.is_empty():
        current = frontier.pop()
        visited[current.location] = 1
        curx = current.location[0]
        cury = current.location[1]
        if curx == 10 and cury == 10:
            retrace(maze,current)
            break
        for next in ((curx,cury-1),(curx,cury+1),(curx+1,cury),(curx-1,cury)):
            #print(next)
            if next[0]>=0 and next[0] <=11 and next[1] >=0 and next[1] <=11 and next not in visited and maze[next[0]][next[1]] !="1":
                frontier.push(space(next,current))
mazeSolver()
