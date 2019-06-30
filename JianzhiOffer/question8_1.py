'''
Find the next node of the given node in inorder travesal
acwing 19
'''
import numpy as np
from BasicDataStructure.Tree.BinaryTree import BinaryTree

def solution1(btree, element):
    node = btree.search(element)
    print(node.value)
    if node.right:
        next_node = btree.inorder_iterative(node.right)[0]

    else:
        parent = node.parent
        if node == parent.left:
            next_node = parent.value
        else:
            grandparent = parent.parent
            next_node = grandparent.value

    return next_node

if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    btree = BinaryTree(element_list)
    inorder = btree.inorder_iterative(btree.root)
    element = np.random.choice(inorder, 1)[0]
    print(inorder, element)
    next_node = solution1(btree, element)
    print(next_node)