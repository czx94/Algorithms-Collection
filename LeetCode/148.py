'''
Sort a linked list, time complexity O(nlgn)
'''

# Definition for singly-linked list.
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        counter = head
        while counter:
            counter += 1
            counter = counter.next

        if count == 1:
            return count
        split_point = math.floor(count / 2)

        left_list = head
        for i in range(self.split_point):
            head = head.next
        right_list = head

        left = self.sortList()
        right = self.sortList()
        list_object = self.merge(left, right)

    def merge(self, list1, list2):

        return combined_list