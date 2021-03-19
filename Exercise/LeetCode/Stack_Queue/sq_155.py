'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
'''
class MinStack():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        if self.stack:
            return min(ele for ele in self.stack)
        else:
            return None



