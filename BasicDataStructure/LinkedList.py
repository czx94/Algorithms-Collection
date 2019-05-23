import numpy as np

class Node(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList(object):
    '''
    First in last out
    '''
    def __init__(self, linkedlist, n):
        self.linkedlist = linkedlist
        self.size = n
        self.root = None
        self.linkedlist_build()
        self.show()

    def linkedlist_build(self):
        self.root = Node(self.linkedlist[0])
        prev = self.root
        for element in self.linkedlist[1:]:
            current_root = Node(element)
            current_root.prev = prev
            prev.next = current_root
            prev = current_root

    def search(self, element):
        root = self.root

        while root:
            if root.val == element:
                return root
            root = root.next
        return False

    def insert(self, element):
        root = self.root

        while root.prev:
            root = root.prev

        root.next = Node(element)
        root.next.prev = root

    def delete(self, element):
        root_to_delete = self.search(element)
        prev_node = root_to_delete.prev
        next_node = root_to_delete.next

        if not prev_node:
            self.root = next_node
        else:
            prev_node.next = next_node
            next_node.prev = prev_node

    def show(self):
        root = self.root

        while root:
            print(root.val)
            root = root.next

if __name__ == '__main__':
    candidate_list = list(np.random.choice(100, size=10, replace=False))
    print(candidate_list)
    linkedlist = LinkedList(candidate_list, 12)



