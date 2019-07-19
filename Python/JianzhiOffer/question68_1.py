'''
Lowest Common Ancestor of a Binary Tree
leetcode 236
'''

def solution1(root, p, q):
    if root in (p, q, None):
        return root

    else:
        left = solution1(root.left, p, q)
        right = solution1(root.left, p, q)

    return root if (left and right) else (left or right)