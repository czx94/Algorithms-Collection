'''
Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True

        if not s:
            return False

        return self.subtree(s, t) | self.isSubtree(s.left, t) | self.isSubtree(s.right, t)

    def subtree(self, s, t):
        if s and t:
            if s.val == t.val:
                return self.subtree(s.left, t.left) and self.subtree(s.right, t.right)
            else:
                return False

        elif s or t:
            return False

        else:
            return True


