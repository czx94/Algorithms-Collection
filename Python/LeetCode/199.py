# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        stack = [[root], []]
        flag = 0
        while stack[flag]:
            while stack[flag]:
                node = stack[flag].pop(0)
                val = node.val
                if node.left:
                    stack[1 - flag].append(node.left)
                if node.right:
                    stack[1 - flag].append(node.right)

            result.append(val)
            stack[flag] = []
            flag = 1 - flag

        return result