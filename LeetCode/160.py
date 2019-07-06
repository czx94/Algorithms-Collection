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


