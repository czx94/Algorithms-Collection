'''
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.recursiveHelper(root, sum)

        return self.count

    def recursiveHelper(self, root, sum):
        if not root:
            return

        if root.left:
            self.recursiveHelper(root.left, sum)

        if root.right:
            self.recursiveHelper(root.right, sum)

        self.test(root, sum)

    def test(self, root, sum):
        if not root:
            return

        if root.val == sum:
            self.count += 1

        if root.left:
            self.test(root.left, sum - root.val)
        if root.right:
            self.test(root.right, sum - root.val)

# better idea
class Solution2(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.path_sums = {0:1}
        self.target = sum
        self.recursiveHelper(root, 0)

        return self.count

    def recursiveHelper(self, root, current_sum):
        if not root:
            return

        current_sum += root.val

        self.count += self.path_sums.get(current_sum - self.target, 0)
        self.path_sums[current_sum] = self.path_sums.get(current_sum, 0) + 1

        self.recursiveHelper(root.left, current_sum)
        self.recursiveHelper(root.right, current_sum)

        # that's important, cause we switch to another branch
        self.path_sums[current_sum] -= 1





