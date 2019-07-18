'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left, upper=root.val) and self.check(root.right, lower=root.val)

    def check(self, root, lower=None, upper=None):
        if not root:
            return True

        if lower != None and root.val <= lower:
            return False

        if upper != None and root.val >= upper:
            return False

        return self.check(root.left, lower=lower, upper=root.val) and self.check(root.right, lower=root.val, upper=upper)