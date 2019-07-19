# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        node = head
        while count < k and node:
            count += 1
            node = node.next

        if count < k:
            return head

        prev, new_head = self.reverseKGroup(head, k)
        head.next = self.reverseKGroup(new_head, k)

        return prev

    def reverse(self, head, count):
        prev, current = None, head

        while count:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count -= 1

        return prev, current























































    #     count, node = 0, head
    #     while node and count < k:
    #         count += 1
    #         node = node.next
    #
    #     if count < k:
    #         return head
    #
    #     new_head, prev = self.reverse(head, k)
    #     head.next = self.reverseKGroup(new_head, k)
    #
    #     return prev
    #
    # def reverse(self, head, count):
    #     prev, cur, nxt = None, head, head
    #     while count > 0:
    #         nxt = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = nxt
    #         count -= 1
    #     return (cur, prev)