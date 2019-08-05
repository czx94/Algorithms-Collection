'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        slow, fast = head, head.next
        if not fast:
            return TreeNode(slow.val)

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next.next
        node = TreeNode(slow.next.val)
        slow.next = None
        node.left = self.dfs(node, left)
        node.right = self.dfs(node, right)

        return node

    def dfs(self, node, head):
        if not head:
            return None

        else:
            slow, fast = head, head.next
            if not fast:
                return TreeNode(slow.val)

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            left = head
            right = slow.next.next
            node = TreeNode(slow.next.val)
            slow.next = None

            node.left = self.dfs(node, left)
            node.right = self.dfs(node, right)

            return node