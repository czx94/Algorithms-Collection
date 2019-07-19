import numpy as np

class Queue(object):
    '''
    First in first out
    '''
    def __init__(self, queue, n):
        self.queue = [''] * n
        for i in range(len(queue)):
            self.queue[i] = queue[i]
        self.head = 0
        self.tail = len(queue)
        self.size = n

    def enqueue(self, element):
        if self.head == ((self.tail + 1) % self.size):
            raise Exception('Queue overflow')
        self.queue[self.tail] = element
        self.tail = (self.tail + 1) % self.size
        print(self.queue, self.head, self.tail)

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('Queue underflow')
        dequeue, self.queue[self.head] = self.queue[self.head], ''
        self.head = (self.head + 1) % self.size
        print(self.queue, self.head, self.tail)

if __name__ == '__main__':
    queue = Queue(list(np.random.choice(100, size=10, replace=False)), 12)
    for i in range(20):
        if round(np.random.random()):
            queue.enqueue(i)
        else:
            element = queue.dequeue()


