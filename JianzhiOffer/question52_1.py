'''
First common node of two linked list
leetcode 160
'''
import copy

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#using stack
def solution1(headA, headB):
    stack1 = list()
    stack2 = list()

    while headA:
        stack1.append(headA)
        headA = headA.next

    while headB:
        stack2.append(headB)
        headB = headB.next

    last_node = None
    while stack1 and stack2:
        top1 = stack1.pop()
        top2 = stack2.pop()
        if top1 == top2:
            last_node = top1

    return last_node

def solution2(headA, headB):
    len1 = 0
    len2 = 0

    copyA = copy.copy(headA)
    copyB = copy.copy(headB)
    while copyA:
        len1 += 1
        copyA = copyA.next

    while copyB:
        len2 += 1
        copyB = copyB.next

    if len1 > len2:
        for _ in range(len1 - len2):
            headA = headA.next
    elif len1 < len2:
        for _ in range(len2 - len1):
            headB = headB.next

    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


if __name__ == '__main__':
   list1 = ListNode(1)
   list2 = ListNode(1)
   print(solution2(list1, list2))
