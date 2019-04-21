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
    def __init__(self, elements_number):
        self.elements_number = elements_number
        self.root = Node()
        self.range = list(range(0, 100))
        self.node_list = []
        self.candidate_list = [self.root]
        self.build_tree()
        self.dot = Digraph(comment='Binary Tree')

    def build_tree(self):
        while self.elements_number > len(self.node_list):
            root = np.random.choice(self.candidate_list, 1)[0]
            self.candidate_list.remove(root)


            root.value = np.random.choice(self.range, 1)[0]
            self.node_list.append(root)

            root.left = Node()
            root.right = Node()

            self.candidate_list.append(root.left)
            self.candidate_list.append(root.right)


    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return

        if not root.left and not root.right:
            print(root.value)
        else:
            self.inorder(root.value)
            print(root.value)
            self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return


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
    binary_tree = BinaryTree(15)
    binary_tree.preorder(binary_tree.root)
    binary_tree.print_tree()