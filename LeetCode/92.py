# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = m
        if count == 1:
            prev_tail = head
            head, prev_tail.next = self.reverse(head, n - m + 1)
        else:
            m_prev = head
            while count - 2:
                count -= 1
                m_prev = m_prev.next

            prev_tail = m_prev.next
            m_prev.next, prev_tail.next = self.reverse(prev_tail, n - m + 1)

        return head

    def reverse(self, head, count):
        prev = None
        current = head
        while count:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count -= 1
        return prev, current

