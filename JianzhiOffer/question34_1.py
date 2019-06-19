'''
Find all paths in a binary tree with sum equal to a given number
must from root to leaf
leetcode 112
leetcode 437
'''

def solution1(root, sum):
    result = []
    if root:
        recursive(root, sum, [], result)

    return result

def recursive(root, sum, current_path, result):
    if not root:
        return

    current_path += [root.val]
    sum -= root.val
    if not root.left and not root.right:
        if not sum:
            result.append(current_path)
            return

    else:
        if root.left:
            recursive(root.left, sum, current_path, result)
        if root.right:
            recursive(root.right, sum, current_path, result)









if __name__ == '__main__':
