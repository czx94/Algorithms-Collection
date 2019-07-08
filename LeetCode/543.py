# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        if not root:
            return self.diameter

        self.maxDepth(root)

        return self.diameter

    def maxDepth(self, root):
        if not root:
            return 0

        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1