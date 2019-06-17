'''
First common node of two linked list
'''
import numpy as np
from BasicDataStructure.LinkedList import LinkedList

#using stack
def solution1(list1, list2):
    stack1 = list()
    stack2 = list()

    while list1:
        stack1.append(list1)
        list1 = list1.next

    while list2:
        stack2.append(list2)
        list2 = list2.next

    last_node = None
    while stack1 and stack2:
        top1 = stack1.pop()
        top2 = stack2.pop()
        if top1 == top2:
            last_node = top1

    return last_node

def solution2(list1, list2):
    len1 = 0
    len2 = 0

    while list1:
        len1 += 1
        list1 = list1.next

    while list2:
        len2 += 1
        list2 = list2.next

    if len1 > len2:
        for _ in range(len1-len2):
            list1 = list1.next
    else:
        for _ in range(len2-len1):
            list2 = list2.next

    while list1:
        if list1 == list2:
            return list1
        list1 = list1.next
        list2 = list2.next

    return None

d

if __name__ == '__main__':
   pass