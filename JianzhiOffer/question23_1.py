'''
the entry of a circle in a linkedlist

leetcode 141
leetcode 142 ！！！
'''
import copy
def solution1(head):
    if not head:
        return head

    fast = head.next
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    else:
        return None

    while head != slow:
        slow = slow.next
        head = head.next

    return True



'''
Plus: the length of the circle
'''
