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
        if not lists:
            return None

        elif len(lists) == 1:
            return lists[0]

        elif len(lists) == 2:
            # if there are two lists, just merge them
            list1 = lists[0]
            list2 = lists[1]
            list3 = head = ListNode(0)

            while list1 and list2:
                if list1.val < list2.val:
                    list3.next = list1
                    list1 = list1.next
                else:
                    list3.next = list2
                    list2 = list2.next
                list3 = list3.next

            if list1:
                list3.next = list1
            if list2:
                list3.next = list2

            return head.next

        else:
            return self.mergeKLists([self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:])])












        #
        # class Solution(object):
        #     def mergeKLists(self, lists):
        #         """
        #         :type lists: List[ListNode]
        #         :rtype: ListNode
        #         """
        # if len(lists) == 1:
        #     return lists[0]
        # elif len(lists) == 2:
        #     merged_list = head = ListNode(0)
        #     list1, list2 = lists
        #
        #     while list1 and list2:
        #         if list1.val < list2.val:
        #             merged_list.next = list1
        #             list1 = list1.next
        #         else:
        #             merged_list.next = list2
        #             list2 = list2.next
        #         merged_list = merged_list.next
        #
        #     if list1:
        #         merged_list.next = list1
        #     elif list2:
        #         merged_list.next = list2
        #
        #     return head.next
        #
        # while len(lists) > 2:
        #     return self.mergeKLists(
        #         [self.mergeKLists(lists[:len(lists) // 2]), self.mergeKLists(lists[len(lists) // 2:])])