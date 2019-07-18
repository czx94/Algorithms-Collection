class Solution(object):
    # recursive
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = self.reverseList1(head.next)
        node = head.next
        node.next = head
        head.next = None

        return new_head

    # iterative
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev, current = None, head
        while current:
            current.next, prev, current = prev, current, current.next

        return prev