import numpy as np
from BinaryTree import *

class BST(BinaryTree):
    def __init__(self, elements):
        super(BST, self).__init__(elements)

    def build_tree(self):
        for element in self.elements:
            self.insert(element)

    def insert(self, element):
        root = self.root
        while root.value:
            if root.value > element:
                if not root.left:
                    root.left = Node()
                root = root.left
            else:
                if not root.right:
                    root.right = Node()
                root = root.right

        root.value = element

    def search(self, element):
        root = self.root
        while root:
            if root.value == element:
                return True
            elif root.value > element:
                root = root.left
            else:
                root = root.right

        return False

if __name__ == '__main__':
    element_list = list(np.random.choice(list(range(100)), 15))
    bst = BST(element_list)
    bst.print_tree()
    print(bst.search(element_list[3]))







