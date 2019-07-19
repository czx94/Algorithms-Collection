'''
Serialize and Deserialize Binary Tree
leetcode 297
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        if root:
            self.preorder(root, result)
            return ','.join(result)
        else:
            return ''

    def preorder(self, root, result):
        if not root:
            result.append('None')

        else:
            result.append(str(root.val))
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        elements = data.split(',')

        root = self.reconstruct(None, elements)
        return root

    def reconstruct(self, root, data):
        if not data:
            return None

        element = data.pop(0)
        if element == 'None':
            return None
        else:
            root = TreeNode(int(element))
            root.left = self.reconstruct(root.left, data)
            root.right = self.reconstruct(root.right, data)

        return root