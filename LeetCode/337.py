# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # too slow
    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        count = 0

        if root.left:
            count += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            count += self.rob(root.right.left) + self.rob(root.right.right)

        return max(count+root.val, self.rob(root.left)+self.rob(root.right))

    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.rob_helper(root, dict())

    def rob_helper2(self, root, hash_map):
        if not root:
            return 0
        if root in hash_map:
            return hash_map[root]

        count = 0

        if root.left:
            count += self.rob_helper2(root.left.left, hash_map) + self.rob_helper2(root.left.right, hash_map)

        if root.right:
            count += self.rob_helper2(root.right.left, hash_map) + self.rob_helper2(root.right.right, hash_map)

        hash_map[root] = count

        return max(count+root.val, self.rob_helper2(root.left, hash_map)+self.rob_helper2(root.right, hash_map))

    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.rob_helper3(root)

        return max(result)

    def rob_helper3(self, root):
        if not root:
            return [0, 0]

        left = self.rob_helper3(root.left)
        right = self.rob_helper3(root.right)
        res = [max(left[0], left[1]) + max(right[0], right[1]), root.val + left[0] + right[0]]

        return res





