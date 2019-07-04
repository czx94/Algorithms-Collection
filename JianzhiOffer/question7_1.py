'''
Reconstruct a binary tree with its preorder and inorder travesal
leetcode 105
'''
import numpy as np
from BasicDataStructure.Tree.BinaryTree import BinaryTree, Node

'''
Recusive solution
'''
def solution1(preorder, inorder):
    btree = BinaryTree()

    def recursive(root, preorder, inorder, left_or_right):
        if preorder:
            sub_root = preorder[0]
            current_root = Node(sub_root)
        else:
            current_root = sub_root = None

        if left_or_right == 'left':
            root.left = current_root
        elif left_or_right == 'right':
            root.right = current_root
        else:
            btree.root = current_root

        if sub_root:
            root_index = inorder.index(sub_root)

            # split inorder
            inorder_left = inorder[:root_index]
            inorder_right = inorder[root_index+1:]

            # split preorder
            preorder_left = preorder[1:1+root_index]
            preorder_right = preorder[1+root_index:]

            #recursion for left subtree
            #for left subtree
            recursive(current_root, preorder_left, inorder_left, 'left')
            # for rigth subtree
            recursive(current_root, preorder_right, inorder_right, 'right')

    recursive(btree.root, preorder, inorder, 'None')

    return btree



'''
Still recursive solution
'''
def solution2(preorder, inorder):
    pass

if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    btree = BinaryTree(element_list)
    preorder = btree.preorder_iterative(btree.root)
    inorder = btree.inorder_iterative(btree.root)
    print(preorder, inorder)
    reconstructed_btree = solution1(preorder, inorder)
    reorder = reconstructed_btree.preorder_iterative(reconstructed_btree.root)
    inorder = reconstructed_btree.inorder_iterative(reconstructed_btree.root)
    print(preorder, inorder)
    reconstructed_btree = solution2(preorder, inorder)
    preorder = reconstructed_btree.preorder_iterative(reconstructed_btree.root)
    inorder = reconstructed_btree.inorder_iterative(reconstructed_btree.root)
    print(preorder, inorder)
