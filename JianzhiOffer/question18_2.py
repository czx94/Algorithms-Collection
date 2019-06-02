from BasicDataStructure.LinkedList import LinkedList
import numpy as np

def solution1(linked_list):
    root = linked_list.root

    prev = None
    node = root

    while node:
        next = node.next
        if next and next.val == node.val:
            # need to delete repeated elements
            new_next = next.next

            if prev == None:
                linked_list.root = new_next
                node = linked_list.root

            else:
                prev.next = new_next
                node = prev.next

        else:
            prev, node = node, next

    return linked_list

if __name__ == '__main__':
    candidate_list = list(np.random.choice(100, size=10, replace=True))
    candidate_list.insert(0, candidate_list[0])
    candidate_list.insert(7, candidate_list[7])
    candidate_list.insert(-1, candidate_list[-1])
    print(candidate_list)
    linkedlist = LinkedList(candidate_list, 12)
    new_linked_list = solution1(linkedlist)
    new_linked_list.show()