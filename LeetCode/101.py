# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # iterative
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        else:
            stack = [root.left, root.right]
            while stack:
                node1 = stack.pop()
                node2 = stack.pop()

                if not node1 and not node2:
                    return True
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False

                else:
                    if node1.left and node2.right:
                        stack += [node1.left, node2.right]
                    elif node1.left or node2.right:
                        return False

                    if node2.left and node1.right:
                        stack += [node2.left, node1.right]
                    elif node2.left or node1.right:
                        return False

            return True

    # recursive
    def isSymmetric2(self, root):
        if not root:
            return True
        else:
            return self.dfs(root.left, root.right)

    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)
