from random import randint
class altQueue:
    def __init__(self):
        self.inputs = []#these are effectively arraystacks right?
        self.outputs = []
        self.size = 0
    def enqueue(self, value):
        self.size+=1
        self.inputs.append(value)
    def dequeue(self):
        self.size -=1
        if len(self.outputs) <=0:
            while(len(self.inputs) > 0):
                self.outputs.append(self.inputs.pop())
        return self.outputs.pop()
    def top(self):
        if len(self.outputs) <=0):
            return self.inputs[1]
        return self.outputs[-1]
    def isEmpty(self):
        return self.size == 0
