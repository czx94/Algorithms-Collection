'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# not really a hard one
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = root.val
        if not root:
            return self.max_sum

        self.recursive(root)
        return self.max_sum

    def recursive(self, root):
        if not root:
            return 0

        left = self.recursive(root.left)
        right = self.recursive(root.right)

        plus = max(left, right, left+right, 0)
        self.max_sum = max(self.max_sum, plus + root.val)
        return max(left, right, 0) + root.val




