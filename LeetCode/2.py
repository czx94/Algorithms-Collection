# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = head = ListNode(0)
        plus = 0
        while l1 and l2:
            sum = l1.val + l2.val + plus
            val = sum % 10
            plus = sum // 10

            node.next = ListNode(val)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + plus
            val = sum % 10
            plus = sum // 10

            node.next = ListNode(val)
            node = node.next
            l1 = l1.next

        while l2:
            sum = l2.val + plus
            val = sum % 10
            plus = sum // 10

            node.next = ListNode(val)
            node = node.next
            l2 = l2.next

        if plus:
            node.next = ListNode(plus)

        return head.next


