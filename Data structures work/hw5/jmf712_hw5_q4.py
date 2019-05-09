from random import randint
class maxStack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.maxVal = None
    def is_empty(self):
        return self.size == 0

    def max(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.maxVal
    def top(self):
        return self.stack[-1][0]

    def len(self):
        return self.size

    def push(self, value):
        if self.size == 0:
            self.stack.append((value,None))
            self.maxVal = value
        elif value >= self.maxVal:
            self.stack.append((value, self.maxVal))
            self.maxVal = value
        else:
            self.stack.append((value, None))
        self.size+=1

    def pop(self):
        self.size -=1
        if self.stack[-1][0] == self.maxVal:
            self.maxVal = self.stack[-1][1]
        return self.stack.pop()[0]

def test():
    failed = False
    for x in range(100):
        test = maxStack()
        control = []
        for x in range(randint(0,100)):
            val = randint(0,100)
            test.push(val)
            control.append(val)

            if test.max() != max(control):
                failed =  True
        while not test.is_empty():
            if test.max() != max(control):
                failed = True
            test.pop()
            control.pop()
    print(failed)
