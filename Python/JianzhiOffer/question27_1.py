'''
Invert Binary Tree
leetcode 226
'''

# recursive
def solution1(root):
    if not root:
        return root

    else:
        left = solution1(root.right)
        right = solution1(root.left)
        root.left = left
        root.right = right

    return root

# iterative
def solution2(root):
    if not root:
        return root

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            left, right = node.left, node.right
            node.left, node.right = right, left
            stack += [left, right]

    return root