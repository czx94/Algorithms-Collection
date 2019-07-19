# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def remove(head):
            if not head:
                return 0, head

            count, head.next = remove(head.next)
            return count + 1, (head, head.next)[count + 1 == n]

        return remove(head)[1]

    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def index(node):
            if not node:
                return 0

            count = index(node.next)

            if count >= n:
                node.next.val = node.val

            return count + 1

        index(head)
        return head.next

    def removeNthFromEnd3(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        for _ in range(n):
            node1 = node1.next

        if not node1:
            head = head.next

        else:
            while node1.next:
                node1 = node1.next
                node2 = node2.next

            node2.next = node2.next.next

        return head
