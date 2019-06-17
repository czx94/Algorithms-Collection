'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

leetcode 110
'''

# stupid, travel repeatedly
def solution1(root):
    if not root:
        return True

    left = get_height1(root.left)
    right = get_height1(root.right)

    if abs(left - right) > 1:
        return False
    return solution1(root.left) and solution1(root.right)

# from question55_1
def get_height1(root):
    if not root:
        return 0
    left = get_height1(root.left)
    right = get_height1(root.right)
    return max(left, right) + 1


def solution2(root):
    global flag
    flag = True

    get_height2(root)

    return flag

def get_height2(root):
    if not root:
        return 0
    left = get_height2(root.left)
    right = get_height2(root.right)
    nonlocal flag
    if abs(left-right) > 1:
        flag = False
    return max(left, right) + 1

def solution3(root):
    result = get_height3(root)

    return result != -1

def get_height3(root):
    if not root:
        return 0
    left = get_height3(root.left)
    right = get_height3(root.right)

    if left == -1 or right == -1:
        return -1
    if abs(left-right) > 1:
        return -1
    return max(left, right) + 1