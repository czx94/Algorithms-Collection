'''
Convert Binary Search Tree to Sorted Doubly Linked List
leetcode 426
'''

class ListNode(object):
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

def solution1(root):
    if not root:
        return None

    return dfs(root)

def dfs(root):
    if not root:
        return None

    current_node = ListNode(root.val, None, None)
    if not root.left and not root.right:
        return current_node

    else:
        if root.left:
            left = dfs(root.left)
            while left and left.next:
                left = left.next
            current_node.prev = left
            left.next = current_node

        if root.right:
            right = dfs(root.right)
            current_node.prev = right
            right.next = current_node

        return current_node



