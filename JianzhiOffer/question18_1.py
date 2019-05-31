from BasicDataStructure.LinkedList import LinkedList
import numpy as np

def solution1(linked_list, node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next

    else:
        root = linkedlist.root
        while root:
            if root.next == node:
                root.next = root.next.next

    return linked_list

if __name__ == '__main__':
    candidate_list = list(np.random.choice(100, size=10, replace=False))
    print(candidate_list)
    linkedlist = LinkedList(candidate_list, 12)
    node = linkedlist.search(candidate_list[3])
    new_linked_list = solution1(linkedlist, node)
    new_linked_list.show()