from Tree.BinarySearchTree import BST
from Tree.BinaryTree import Node
import numpy as np
import uuid
import os
from graphviz import Digraph


class RBNode(Node):
    def __init__(self, value = None, left = None, right = None, color = 'BLACK', parent = None):
        super(RBNode, self).__init__(value, left, right)
        self.color = color
        self.parent = parent

    def show_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

class RBTree(BST):
    '''
    5 rules:
    1.Each node is either red or black.
    2.The root is black.
    3.All leaves (NIL) are black.
    4.If a node is red, then both its children are black.
    5.Every path from a given node to any of its dscendant NIL nodes contains the same number of black nodes.
    '''
    def __init__(self, elements):
        self.nil = RBNode()
        root = RBNode(color='BLACK')
        super(RBTree, self).__init__(elements, root = root)

    # find the node with value key
    def find(self, key, node):
        if not node:
            return None
        elif key < node.data:
            return self.find(key, node.left)
        elif key > node.data:
            return self.find(key, node.right)
        else:
            return node

    def tree_minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def transplant(self, tree, node_u, node_v):
        """
        exchange node v and u
        :param tree: tree root
        :param node_u: node to be replaced
        :param node_v: node to replace
        :return: None
        """
        if not node_u.parent:
            tree.root = node_v
        elif node_u == node_u.parent.left:
            node_u.parent.left = node_v
        elif node_u == node_u.parent.right:
            node_u.parent.right = node_v
        # 加一下为空的判断
        if node_v:
            node_v.parent = node_u.parent

    def left_rotate(self, node):
        '''
             *     parent               parent
             *    /                       /
             *   node                   right
             *  / \                     / \
             * ln  right   ----->     node  ry
             *    / \                 / \
             *   ly ry               ln ly
        '''
        parent = node.parent
        right = node.right

        # 1
        node.right = right.left
        if right.left != self.nil:
            right.left.parent = node.right

        # 2
        right.left = node
        node.parent = right

        # 3
        right.parent = parent
        if parent == self.nil:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

    def right_rotate(self, node):
        '''
             *        parent           parent
             *       /                   /
             *      node                left
             *     /    \               / \
             *    left  ry   ----->   ln  node
             *   / \                     / \
             * ln  rn                   rn ry
        '''
        parent = node.parent
        left = node.left

        # 1
        node.left = left.right
        if left.right != self.nil:
            left.right.parent = node.left

        # 2
        left.right = node
        node.parent = left

        # 3
        left.parent = parent
        if parent == self.nil:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

    def insert(self, value):
        root = self.root
        node = RBNode(value=value, color='RED')
        node.left = self.nil
        node.right = self.nil
        node.parent = self.nil

        if not root.value:
            node.color = 'BLACK'
            self.root = node

        else:
            while root != self.nil:
                current_parent = root
                if value < root.value:
                    root = root.left
                else:
                    root = root.right

            if value < current_parent.value:
                current_parent.left = node
            else:
                current_parent.right = node
            node.parent = current_parent

            self.insert_fixup(node)


    def insert_fixup(self, node):
        # if node parent is black or node is root then everything is ok
        while node.parent.color == "RED":
            # node.parent.parent must exist because node.parent is red
            # we deal the left situation first then right
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                # case 1: uncle is red
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BlACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent

                else:
                    # case 2: uncle is black and node is right child
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    # case 3: uncle is black and node is left child
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)

            # symetry
            else:
                uncle = node.parent.parent.left

                # case 1: uncle is red
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BlACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent

                else:
                    # case 2: uncle is black and node is left child
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    # case 3: uncle is black and node is right child
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)

        # keep root color black!
        self.root.color = "BLACK"

    def print_tree(self, label=True):
        dot = Digraph(comment='RBTree')

        def print_node(node, node_tag):
            if node.left != self.nil:
                left_tag = str(uuid.uuid1())
                color = node.left.color
                if color == 'RED':
                    color = 'red'
                else:
                    color = 'green'
                dot.node(left_tag, ':'.join([str(node.left.value), str(node.left.order)]), style='filled', color=color)
                label_string = 'L' if label else ''
                dot.edge(node_tag, left_tag, label=label_string)
                print_node(node.left, left_tag)

            if node.right != self.nil:
                right_tag = str(uuid.uuid1())
                color = node.right.color
                if color == 'RED':
                    color = 'red'
                else:
                    color = 'green'
                dot.node(right_tag, ':'.join([str(node.right.value), str(node.right.order)]), style='filled', color=color)
                label_string = 'R' if label else ''
                dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        if self.root:
            root_tag = str(uuid.uuid1())
            color = self.root.color
            if color == 'RED':
                color = 'red'
            else:
                color = 'green'
            dot.node(root_tag, ':'.join([str(self.root.value), str(self.root.order)]), style='filled', color=color)
            print_node(self.root, root_tag)

        # define file name by script name
        base_name = os.path.basename(__file__)[:-3]
        save_path = base_name +'.gv'
        dot.render(save_path)

    def delete(self, node):
        current_node = node
        current_node_color = current_node.color

        if node.left == self.nil:
            temp = node.right
            self.transplant(node, node.right)

        elif node.right == self.nil:
            temp = node.left
            self.transplant(node, node.left)

        else:
            current_node = self.tree_minimum(node.right)
            current_node_color = current_node.color
            temp = current_node.right

            if current_node.parent == node:
                temp.parent = current_node
            else:
                self.transplant(current_node, current_node.right)
                current_node.right = node.right
                current_node.parent = current_node

            self.transplant(node, current_node)
            current_node.left = node.left
            current_node.left.parent = current_node
            current_node.color = node.color

        if current_node_color == 'BLACK':
            self.delete_fixup(temp)


    def delete_fixup(self, node):
        while node != self.root and node.color == 'BLACK':
            # deal with left child situation
            if node == node.parent.left:
                brother = node.parent.right
                # case 1
                if brother.color == 'RED':
                    brother.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.right_rotate(node.parent)
                    brother = node.parent.right

                # case 2
                if brother.left.color == 'BLACK' and brother.right.color == 'BLACK':
                    brother.color = 'RED'
                    node = node.parent
                else:
                    # case 3
                    if brother.right.color == 'BLACK':
                        brother.left.color = 'BLACK'
                        brother.color = 'RED'
                        self.right_rotate(brother)
                        brother = node.parent.right

                    # case 4
                    brother.color = node.parent.color
                    node.parent.color = 'BLACK'
                    brother.right.color = 'BLACK'
                    self.left_rotate(node.parent)
                    node = self.root

            # deal with right child situation
            else:
                brother = node.parent.left
                if brother.color == 'RED':
                    brother.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.left_rotate(node.parent)
                    brother = node.parent.left

                if brother.right.color == 'BLACK' and brother.left.color == 'BLACK':
                    brother.color = 'RED'
                    node = node.parent
                else:
                    if brother.left.color == 'BLACK':
                        brother.right.color = 'BLACK'
                        brother.color = 'RED'
                        self.left_rotate(brother)
                        brother = node.parent.left

                    brother.color = node.parent.color
                    node.parent.color = 'BLACK'
                    brother.left.color = 'BLACK'
                    self.right_rotate(node.parent)
                    node = self.root

        node.color = 'BLACK'



    def preorder(self, root):
        if not root.value:
            return

        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

if __name__ == '__main__':
    #unsolved cases
    element_list = list(np.random.choice(list(range(100)), 10, replace=False))
    print(element_list)
    rb_tree = RBTree(element_list)
    # rb_tree.preorder(rb_tree.root)
    rb_tree.print_tree()