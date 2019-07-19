import numpy as np

class Stack(object):
    '''
    First in last out
    '''
    def __init__(self, stack, n):
        self.stack = stack
        self.top = len(self.stack)
        self.size = n

    def push(self, element):
        if self.top == self.size:
            raise Exception('Stack overflow')
        self.stack.append(element)
        self.top += 1
        print(self.stack, self.top)

    def pop(self):
        if self.top == 0:
            raise Exception('Stack underflow')
        self.stack.pop()
        self.top -= 1
        print(self.stack, self.top)

    def stack_empty(self):
        if self.top:
            return False
        else:
            return True

if __name__ == '__main__':
    stack = Stack(list(np.random.choice(100, size=10, replace=False)), 12)
    stack.push(11)
    stack.push(11)
    stack.push(11)
    n = stack.pop()


