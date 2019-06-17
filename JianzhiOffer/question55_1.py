'''
Max depth of a tree
leetcode 104
'''

def solution1(root):
    if not root:
        return 0

    return max(solution1(root.left), solution1(root.right)) + 1