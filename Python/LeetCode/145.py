class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive one
        self.result = []

        if root:
            self.recursive(root)

        return self.result

    def recursive(self, root):
        if not root.left and not root.right:
            self.result.append(root.val)

        else:
            if root.left:
                self.recursive(root.left)
            if root.right:
                self.recursive(root.right)
            self.result.append(root.val)

class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative one
        result = []
        if root:
            stack = [root]
            final_list = []

            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                final_list.append(node)


            while final_list:
                node = final_list.pop()
                result.append(node.val)

        return result
