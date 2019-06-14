# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# just recursive, easier than imaging
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            merged_list = head = ListNode(0)
            list1, list2 = lists

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

        while len(lists) > 2:
            return self.mergeKLists(
                [self.mergeKLists(lists[:len(lists) // 2]), self.mergeKLists(lists[len(lists) // 2:])])