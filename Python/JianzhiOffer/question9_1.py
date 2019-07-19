'''
Implemente a queue with two stacks
leetcode 232
'''
import numpy as np

class Queue(object):
    '''
    First in first out
    '''
    def __init__(self, elements):
        self.stack1 = list()
        self.stack2 = list()
        self.head = None
        self.tail = None

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                data = self.stack1.pop()
                self.stack2.append(data)

        if not self.stack2:
            raise Exception('Empty queue')

        head = self.stack2.pop()

        return head

if __name__ == '__main__':
    pass