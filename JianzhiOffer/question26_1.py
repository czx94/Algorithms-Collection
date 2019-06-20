'''
Subtree of a given tree?
leetcode 572
'''


def solution1(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    result = False

    if s and t:
        if s.val == t.val:
            result = include(s, t)
        if not result:
            result = solution1(s.left, t)
        if not result:
            result = solution1(s.right, t)

    return result


def include(t1, t2):
    # if not t2 and not t1:
    #     return True
    #
    # if not t2 or not t1:
    #     return False

    # depends on definition here
    if not t2:
        return True
    if not t1:
        return False

    if t1.val != t2.val:
        return False

    return include(t1.left, t2.left) and include(t1.right, t2.right)