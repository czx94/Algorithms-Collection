'''
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.value = root.val
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return True

        if self.value != root.val:
            return False

        return self.dfs(root.left) and self.dfs(root.right)