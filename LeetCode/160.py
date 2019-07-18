# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        len_b = 0

        a = headA
        while a:
            len_a += 1
            a = a.next

        b = headB
        while b:
            len_b += 1
            b = b.next

        if len_a < len_b:
            headA, headB = headB, headA
            len_a, len_b = len_b, len_a

        for _ in range(len_a - len_b):
            headA = headA.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = []
        b = []
        while headA:
            a.append(headA)
            headA = headA.next
        while headB:
            b.append(headB)
            headB = headB.next

        intersect = None
        for i in range(1, min(len(a), len(b))+1):
            if a[-i] == b[-i]:
                print(999)
                intersect = a[-i]
            else:
                break

        return intersect

    # find the loop of the concat list
    def getIntersectionNode3(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        last = headA
        while last.next:
            last = last.next

        last.next = headB

        slow = headA
        fast = headA

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # like find the entry of a loop in likedlist
                fast = headA
                while fast != slow:
                    fast, slow = fast.next, slow.next

                last.next = None
                return slow

        last.next = None
        return None

    def getIntersectionNode4(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = headB if nodeA == None else nodeA.next
            nodeB = headA if nodeB == None else nodeB.next

        return nodeA
