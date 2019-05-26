'''
Print each node of a linkedlist from end to start
'''
from BasicDataStructure.LinkedList import LinkedList
import numpy as np

# stack
def solution1(linkedlist):
    print('Stack solution')
    stack = []
    root = linkedlist.root
    while root:
        stack.append(root.val)
        root = root.next

    while stack:
        val = stack.pop()
        print(val)

# recursive
def solution2(linkedlist):
    print('Recursive solution')
    def recursion(root):
        if root.next:
            recursion(root.next)
        print(root.val)

    root = linkedlist.root
    recursion(root)

if __name__ == '__main__':
    list_elements = list(np.random.choice(100, size=10, replace=False))
    print(list_elements)
    linkedlist = LinkedList(list_elements, 12)
    solution1(linkedlist)
    solution2(linkedlist)
