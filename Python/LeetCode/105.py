class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree1(self, preorder, inorder):
        root = TreeNode(0)
        self.dfs(preorder, inorder, root, 'left')
        return root.left

    def dfs(self, preorder, inorder, root, left_or_right):
        if preorder:
            sub_root = preorder[0]
            current_root = TreeNode(sub_root)
        else:
            current_root = sub_root = None

        if left_or_right == 'left':
            root.left = current_root
        elif left_or_right == 'right':
            root.right = current_root

        if current_root:
            root_index = inorder.index(sub_root)

            # split inorder
            inorder_left = inorder[:root_index]
            if root_index != len(inorder) - 1:
                inorder_right = inorder[root_index + 1:]
            else:
                inorder_right = []

            # split preorder
            preorder_left = preorder[1:1 + len(inorder_left)]
            preorder_right = preorder[1 + len(inorder_left):]

            self.dfs(preorder_left, inorder_left, current_root, 'left')
            self.dfs(preorder_right, inorder_right, current_root, 'right')

    def buildTree2(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            ind = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder[:ind], inorder[:ind])
            root.right = self.buildTree(preorder[ind:], inorder[ind + 1:])
            return root


if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree2(preorder, inorder)


