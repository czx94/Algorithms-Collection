# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    # recursive
    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST1(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST1(root.left)

        return root

    # iterative
    def convertBST2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0
        stack = []

        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left

        return root