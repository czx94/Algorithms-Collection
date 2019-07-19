'''
Copy List with Random Pointer
leetcode 138
'''

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

def solution1(head):
    if not head:
        return head

    # copy the linkedlist
    pointer = head
    while pointer:
        this = Node(pointer.val, pointer.next, None)
        pointer.next = this
        pointer = pointer.next.next

    # copy the random links
    pointer = head
    while pointer:
        if pointer.random:
            pointer.next.random = pointer.random.next
        pointer = pointer.next.next

    # remove the old ones
    new_head = head.next
    new_pointer = new_head
    old_pointer = head
    while new_pointer.next:
        # recover old list
        old_pointer.next = new_pointer.next
        old_pointer = old_pointer.next

        # construct new one
        new_pointer.next = old_pointer.next
        new_pointer = new_pointer.next

    new_pointer.next = None
    old_pointer.next = None
    return new_head