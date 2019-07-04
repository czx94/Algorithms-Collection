'''
Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string
and this string can be deserialized to the original tree structure.

level travesal
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
        if not root:
            return []

        flag = 0
        stack = [[root], []]
        serie = []
        while stack[flag]:
            for node in stack[flag]:
                if node:
                    serie.append(str(node.val))
                    stack[1 - flag] += [node.left, node.right]
                else:
                    serie.append('None')

            stack[flag] = []
            flag = 1 - flag

        return serie

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        root = TreeNode(data.pop(0))
        stack = [root]
        while stack and data:
            node = stack.pop(0)
            if node:
                left_val = data.pop(0)
                if left_val == 'None':
                    node.left = None
                else:
                    node.left = TreeNode(int(left_val))
                stack.append(node.left)

                right_val = data.pop(0)
                if right_val == 'None':
                    node.right = None
                else:
                    node.right = TreeNode(int(right_val))
                stack.append(node.right)

        return root