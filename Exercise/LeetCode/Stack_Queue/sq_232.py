'''
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''
class Solution():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        ele = self.stack[0]
        for i in range(1, len(self.stack)):
            self.stack[i - 1] = self.stack[i]
        self.stack.pop()
        print(ele)

    def peek(self):
        print(self.stack[0])

    def empty(self):
        print(not self.stack)   # important

queue = Solution()
queue.push(1)
queue.push(2)
queue.peek()
queue.pop()
queue.empty()
