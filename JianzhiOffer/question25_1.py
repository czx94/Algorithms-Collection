'''
Merge two sorted list
leetcode 23
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def solution1(list1, list2):
    merged_list = head = ListNode(0)

    while list1 and list2:
        if list1.val < list2.val:
            merged_list.next = list1
            list1 = list1.next
        else:
            merged_list.next = list2
            list2 = list2.next
        merged_list = merged_list.next

    if list1:
        merged_list.next = list1
    elif list2:
        merged_list.next = list2

    return head.next