import numpy as np

class Node(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList(object):
    '''
    First in last out
    '''
    def __init__(self, linkedlist, n):
        self.linkedlist = linkedlist
        self.size = n

    def search(self, element):
        pass

    def insert(self, element):
        pass

    def delete(self, element):
        pass

if __name__ == '__main__':
    linkedlist = LinkedList(list(np.random.choice(100, size=10, replace=False)), 12)



