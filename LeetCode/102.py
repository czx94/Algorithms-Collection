# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = list()
        if root:
            self.stacks = [[root], []]
            flag = 0
            while self.stacks[flag]:
                current_level = list()
                for node in self.stacks[flag]:
                    current_level.append(node.val)
                    if node.left:
                        self.stacks[1 - flag].append(node.left)
                    if node.right:
                        self.stacks[1 - flag].append(node.right)

                self.stacks[flag] = []
                result.append(current_level)
                flag = 1 - flag

        return result