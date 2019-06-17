import numpy as np
from graphviz import Digraph
import uuid
import os

class Node(object):
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.order = None
        self.parent = parent


class BinaryTree(object):
    '''
    Common binary tree, generated randomly
    Support several travesal methods
    '''
    def __init__(self, elements=[], root=None):
        self.elements = elements
        self.root = root

        self.build_tree()

        # object to viz tree
        self.dot = Digraph(comment='Binary Tree')

        # define the order to visit a node
        self.count = 0

    # build the binary tree with given elements
    def build_tree(self):
        for element in self.elements:
            self.insert(element)

    # insert element randomly
    def insert(self, element):
        root = self.root
        if not root:
            self.root = Node(element)
            return

        while root.value:
            parent = root
            if np.random.random() > 0.5:
                if not root.left:
                    root.left = Node()
                root = root.left
            else:
                if not root.right:
                    root.right = Node()
                root = root.right

        root.value = element
        root.parent = parent

    def insert_to_node(self, root, element, subtree='left'):
        if subtree == 'left':
            root.left = Node(element)
        else:
            root.right = Node(element)

    # preorder recursive travesal
    def preorder(self, root):
        if not root:
            return

        root.order = self.count
        self.count += 1

        self.preorder(root.left)
        self.preorder(root.right)

    # preorder iterative travesal
    def preorder_iterative(self, root):
        order_list = []
        candidate_nodes = [root]
        while candidate_nodes:
            current_node = candidate_nodes.pop()
            if current_node:
                current_node.order = self.count
                self.count += 1
                order_list.append(current_node.value)
                candidate_nodes.append(current_node.right)
                candidate_nodes.append(current_node.left)

        return order_list

    # inorder recursive travesal
    def inorder(self, root):
        if not root:
            return

        if not root.left and not root.right:
            root.order = self.count
            self.count += 1

        else:
            self.inorder(root.left)

            root.order = self.count
            self.count += 1

            self.inorder(root.right)

    # inorder iterative travesal
    def inorder_iterative(self, root):
        order_list = []
        candidate_nodes = []
        while candidate_nodes or root:
            # visit always the left subtree till the end and append it to the stack
            while root:
                candidate_nodes.append(root)
                root = root.left

            # while there's no left subtree, pop the stack and note the node then visit the right subtree
            root = candidate_nodes.pop()
            if root:
                root.order = self.count
                self.count += 1
                order_list.append(root.value)
                root = root.right

        return order_list

    # postorder resursive travesal
    def postorder(self, root):
        if not root:
            return

        if not root.left and not root.right:
            root.order = self.count
            self.count += 1

        else:
            self.postorder(root.left)

            self.postorder(root.right)

            root.order = self.count
            self.count += 1

    # postorder iterative travesal
    def postorder_iterative(self, root):
        order_list = []
        candidate_nodes = [root]
        final_iteration = []

        # visit the nodes with reverse order: parent, right, left
        # so the nodes are pushed to a stack with order: left, right, parent
        while candidate_nodes:
            current_node = candidate_nodes.pop()
            if current_node.left:
                candidate_nodes.append(current_node.left)
            if current_node.right:
                candidate_nodes.append(current_node.right)

            final_iteration.append(current_node)

        # just pop the stack iteratively
        while final_iteration:
            node = final_iteration.pop()
            node.order = self.count
            self.count += 1
            order_list.append(node.value)

        return order_list

    # levelorder travesal using 2 stacks
    def levelorder(self):
        order_list = []
        candidate_layer = [self.root]

        while candidate_layer:
            this_layer, candidate_layer = candidate_layer, []

            for node in this_layer:
                node.order = self.count
                self.count += 1
                order_list.append(node.value)

                if node.left:
                    candidate_layer.append(node.left)
                if node.right:
                    candidate_layer.append(node.right)

        return order_list

    def search(self, element):
        '''
        :param element: the value of the node to search
        :return: the searched node, if not existing return False
        '''
        candidates = [self.root]
        while candidates:
            current_node = candidates.pop()
            if current_node:
                if current_node.value == element:
                    return current_node
                else:
                    candidates += [current_node.left, current_node.right]

        return False


    def print_tree(self, label=True):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        def print_node(node, node_tag):
            color = np.random.choice(colors, 1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())
                self.dot.node(left_tag, ':'.join([str(node.left.value), str(node.left.order)]), style='filled', color=color)
                label_string = 'L' if label else ''
                self.dot.edge(node_tag, left_tag, label=label_string)
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, ':'.join([str(node.right.value), str(node.right.order)]), style='filled', color=color)
                label_string = 'R' if label else ''
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        if self.root is not None:
            root_tag = str(uuid.uuid1())
            self.dot.node(root_tag, ':'.join([str(self.root.value), str(self.root.order)]), style='filled', color=np.random.choice(colors, 1)[0])
            print_node(self.root, root_tag)

        # define file name by script name
        base_name = os.path.basename(__file__)[:-3]
        save_path = base_name +'.gv'
        self.dot.render(save_path)

if __name__ == '__main__':
    element_list = list(np.random.choice(list(range(100)), 15))
    binary_tree = BinaryTree(element_list)
    print(binary_tree.inorder_iterative(binary_tree.root))
    binary_tree.print_tree()