'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[1]

    def dfs(self, root):
        if not root:
            return 0, True

        left_height, l = self.dfs(root.left)
        right_height, r = self.dfs(root.right)

        if l and r and abs(left_height - right_height) <= 1:
            return max(left_height, right_height) + 1, True
        else:
            return 0, False
