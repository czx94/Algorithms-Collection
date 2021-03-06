'''
Reverse linkedlist
leetcode 206
leetcode 92
leetcode 25
'''
import copy

# stupid
def solution1(head):
    if not head:
        return head

    temp = []
    pointer1 = copy.copy(head)

    while pointer1:
        temp.append(pointer1.val)
        pointer1 = pointer1.next

    head.val = temp.pop()
    pointer2 = copy.copy(head)
    head = head.next
    while head:
        head.val = temp.pop()
        head = head.next

    return pointer2

# iterative
def solution2(head):
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current

    return prev

# recursive
def solution3(head):
    if not head or not head.next:
        return head

    new_head = solution3(head.next)
    next_node = head.next
    next_node.next = head
    head.next = None

    return new_head