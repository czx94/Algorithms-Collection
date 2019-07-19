# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.right)
        if not root.left:
            return
        self.flatten(root.left)

        node = root.left
        while node.right:
            node = node.right

        root.left, root.right, node.right = None, root.left, root.right

