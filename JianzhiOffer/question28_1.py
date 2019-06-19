'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
leetcode 101
'''

# level order travelsal and ...
def solution1(root):
    result = list()
    if root:
        stacks = [[root], []]
        flag = 0
        while stacks[flag]:
            current_level = list()
            for node in stacks[flag]:
                if node:
                    current_level.append(node.val)
                    stacks[1 - flag].append(node.left)
                    stacks[1 - flag].append(node.right)
                else:
                    current_level.append(-1)

            stacks[flag] = []
            result.append(current_level)
            flag = 1 - flag

    for layer in result:
        if layer != layer[::-1]:
            return False
    return True

# recursive
def solution2(root):
    if not root:
        return True
    else:
        return dfs(root.left, root.right)

def dfs(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False

    if left.val == right.val:
        return dfs(left.left, right.right) and dfs(right.left, left.right)

    else:
        return False


# iterative
def solution3(root):
    if not root:
        return True

    stack = [[root.left, root.right]]

    while stack:
        node = stack.pop(0)
        left = node.left
        right = node.right

        if not left and not right:
            continue
        if not left or not right:
            return False

        if left.val == right.val:
            stack.append(0, [left.left, right.right])
            stack.append(0, [left.right, right.left])
        else:
            return False



if __name__ == '__main__':
