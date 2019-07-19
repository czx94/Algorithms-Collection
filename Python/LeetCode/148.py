'''
Sort a linked list, time complexity O(nlgn)
'''

# Definition for singly-linked list.
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# solution 1: split list by counting
class Solution1(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next

        if count == 1 or count == 0:
            return head
        elif count == 2:
            if head.val > head.next.val:
                head.val, head.next.val = head.next.val, head.val
                return head

        split_point = count // 2 - 1

        left_list = head
        for i in range(split_point):
            head = head.next
        right_list = head.next
        head.next = None

        left = self.sortList(left_list)
        right = self.sortList(right_list)
        list_object = self.merge(left, right)

        return list_object

    def merge(self, list1, list2):
        temp_list = []
        while list1 and list2:
            if list1.val < list2.val:
                temp_list.append(list1)
                list1 = list1.next
            else:
                temp_list.append(list2)
                list2 = list2.next

        while list1:
            temp_list.append(list1)
            list1 = list1.next

        while list2:
            temp_list.append(list2)
            list2 = list2.next

        combined_list = temp_list[0]
        node = combined_list

        for i in range(1, len(temp_list)):
            node.next = temp_list[i]
            node = node.next

        return combined_list

# solution 2: split list by slow and fast pointers
class Solution2(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, list1, list2):
        dummy = tail = ListNode(None)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next, tail, list1 = list1, list1, list1.next
            else:
                tail.next, tail, list2 = list2, list2, list2.next

        tail.next = list1 or list2
        return dummy.next