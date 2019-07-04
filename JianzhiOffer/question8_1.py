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
        node = node.right
        while node.left:
            node = node.left
        return node

    elif node.parent:
        parent = node.parent
        if node == parent.left:
            return parent
        else:
            if parent.parent:
                return parent.parent

    return None

# correct one
def solution2(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.father:
        father = node.father
        if node == father.left:
            return father
        node = father

    return None

if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    btree = BinaryTree(element_list)
    inorder = btree.inorder_iterative(btree.root)
    element = np.random.choice(inorder, 1)[0]
    print(inorder, element)
    next_node = solution1(btree, element)
    print(next_node)