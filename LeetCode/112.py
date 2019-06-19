def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False

    if not root.left and not root.right:
        return sum == root.val

    else:
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)