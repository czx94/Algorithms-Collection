from Tree.BinaryTree import *


class BST(BinaryTree):
    def __init__(self, elements, root=None):
        super(BST, self).__init__(elements, root=root)
        # object to viz tree

    def build_tree(self):
        for element in self.elements:
            self.insert(element)

    def insert(self, element):
        root = self.root
        if not root:
            self.root = Node(element)
            return

        parent = root
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
        root.parent = parent

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
    print(element_list)
    bst = BST(element_list)
    bst.inorder(bst.root)
    bst.print_tree()
    print(bst.search(element_list[3]))