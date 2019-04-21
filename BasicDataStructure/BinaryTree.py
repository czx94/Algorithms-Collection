import numpy as np
from graphviz import Digraph
import uuid

class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.order = 0


class BinaryTree(object):
    def __init__(self, elements):
        self.elements = elements
        self.root = Node()

        self.build_tree()

        # object to viz tree
        self.dot = Digraph(comment='Binary Tree')

        # define the order to visit a node
        self.count = 0

    def build_tree(self):
        elements = self.elements
        node_list = []
        candidate_list = [self.root]
        while elements:
            root = np.random.choice(candidate_list, 1)[0]
            candidate_list.remove(root)

            root.value = elements.pop()
            node_list.append(root)

            root.left = Node()
            root.right = Node()

            candidate_list.append(root.left)
            candidate_list.append(root.right)

    def preorder(self, root):
        if not root or not root.value:
            return

        print(root.value)
        root.order = self.count
        self.count += 1

        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root or not root.value:
            return

        if not root.left.value and not root.right.value:
            print(root.value)
            root.order = self.count
            self.count += 1

        else:
            self.inorder(root.left)

            print(root.value)
            root.order = self.count
            self.count += 1

            self.inorder(root.right)

    def postorder(self, root):
        if not root or not root.value:
            return

        if not root.left.value and not root.right.value:
            print(root.value)
            root.order = self.count
            self.count += 1

        else:
            self.inorder(root.left)

            self.inorder(root.right)

            print(root.value)
            root.order = self.count
            self.count += 1

    def levelorder(self):
        candidate_layer = [self.root]

        while candidate_layer:
            this_layer, candidate_layer = candidate_layer, []

            for node in this_layer:
                print(node.value)
                node.order = self.count
                self.count += 1

                if node.left.value:
                    candidate_layer.append(node.left)
                if node.right.value:
                    candidate_layer.append(node.right)

    def search(self):
        raise Exception('Not implemented error')

    def insert(self):
        raise Exception('Not implemented error')

    def print_tree(self, save_path='./Binary_Tree.gv', label=True):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        def print_node(node, node_tag):
            color = np.random.choice(colors, 1)[0]
            if node.left is not None and node.left.value:
                left_tag = str(uuid.uuid1())
                self.dot.node(left_tag, ':'.join([str(node.left.value), str(node.left.order)]), style='filled', color=color)
                label_string = 'L' if label else ''
                self.dot.edge(node_tag, left_tag, label=label_string)
                print_node(node.left, left_tag)

            if node.right is not None and node.right.value:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, ':'.join([str(node.right.value), str(node.right.order)]), style='filled', color=color)
                label_string = 'R' if label else ''
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        if self.root is not None:
            root_tag = str(uuid.uuid1())
            self.dot.node(root_tag, ':'.join([str(self.root.value), str(self.root.order)]), style='filled', color=np.random.choice(colors, 1)[0])
            print_node(self.root, root_tag)

        self.dot.render(save_path)

if __name__ == '__main__':
    binary_tree = BinaryTree(list(np.random.choice(list(range(100)), 15)))
    binary_tree.levelorder()
    binary_tree.print_tree()