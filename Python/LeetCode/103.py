# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [[root], []]
        flag = 0
        order = []
        while stack[flag] != [None]*len(stack[flag]):
            this_layer = []
            while stack[flag]:
                node = stack[flag].pop()
                if node:
                    this_layer.append(node.val)
                    if flag:
                        stack[1-flag] += [node.right, node.left]
                    else:
                        stack[1-flag] += [node.left, node.right]

            stack[flag] = []
            flag = 1 - flag
            order.append(this_layer)

        return order



