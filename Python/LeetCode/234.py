# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse = None
        slow, fast = head, head

        while fast and fast.next:
            reverse, reverse.next, slow, fast = slow, reverse, slow.next, fast.next.next

        if fast:
            slow = slow.next

        while slow:
            if reverse.val != slow.val:
                return False
            reverse = reverse.next
            slow = slow.next

        return True