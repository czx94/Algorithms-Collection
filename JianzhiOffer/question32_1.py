'''
Level travel
leetcode 102
'''

def solution1(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = list()
    if root:
        stacks = [[root], []]
        flag = 0
        while stacks[flag]:
            current_level = list()
            for node in stacks[flag]:
                current_level.append(node.val)
                if node.left:
                    stacks[1 - flag].append(node.left)
                if node.right:
                    stacks[1 - flag].append(node.right)

            stacks[flag] = []
            result.append(current_level)
            flag = 1 - flag

    return result