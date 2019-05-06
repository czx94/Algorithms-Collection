from BinarySearchTree import BST
from BinaryTree import Node
import numpy as np

class RBNode(Node):
    def __init__(self, value = None, left = None, right = None, color = None, parent = None):
        super(RBNode, self).__init__(value, left, right)
        self.color = color
        self.parent = parent

    def show_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

class RBTree(BST):
    '''
    Each node is either red or black.
    The root is black.
    All leaves (NIL) are black.
    If a node is red, then both its children are black.
    Every path from a given node to any of its dscendant NIL nodes contains the same number of black nodes.
    '''
    def __init__(self, elements):
        super(RBTree, self).__init__(elements)

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


    def findMin(self, node):
        """
        find the elment with min value among subnode in node
        :param node: the root of the subtree
        :return: the min node
        """
        temp_node = node
        while temp_node.left:
            temp_node = temp_node.left
        return temp_node

    def findMax(self, node):
        """
        find the elment with max value among subnode in node
        :param node: the root of the subtree
        :return: the max node
        """
        temp_node = node
        while temp_node.right:
            temp_node = temp_node.right
        return temp_node

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
        rl = right.left
        node.right = rl
        if rl:
            rl.parent = node.right

        # 2
        right.left = node
        node.parent = right

        # 3
        right.parent = parent
        if not parent:
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
        if node.left:
            node.left.parent = node
        # 2
        left.right = node
        node.parent = left
        # 3
        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

    def insert(self, node):
        # find the nearest node
        temp_root = self.root
        temp_node = None
        while temp_root:
            temp_node = temp_root
            if node.value > temp_node.value:
                temp_root = temp_root.right
            else:
                temp_root = temp_root.left

        # insert the node
        if not temp_node:
            # insert_case1
            self.root = node
            node.color = "BLACK"
        else:
            if node.value < temp_node.value:
                temp_node.left = node
                node.parent = temp_node
            else:
                temp_node.right = node
                node.parent = temp_node
            # fixup for the rules
            self.insert_fixup(node)

    def insert_fixup(self, node):
        # if node parent is black then everything is ok
        while node.parent and node.parent.color == "RED":
            # grandparent must exist cause if not node.parent is root and it's black
            if node.parent == node.parent.parent.left:
                node_uncle = node.parent.parent.right
                # 1. 没有叔叔节点 若此节点为父节点的右子 则先左旋再右旋 否则直接右旋
                # 2. 有叔叔节点 叔叔节点颜色为黑色
                # 3. 有叔叔节点 叔叔节点颜色为红色 父节点颜色置黑 叔叔节点颜色置黑 祖父节点颜色置红 continue
                # 注: 1 2 情况可以合为一起讨论 父节点为祖父节点右子情况相同 只需要改指针指向即可
                if node_uncle and node_uncle.color == "RED":
                    # insert_case3
                    node.parent.color = "BLACK"
                    node_uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                    continue
                elif node == node.parent.right:
                    # insert_case4
                    self.left_rotate(node.parent)
                    node = node.left
                # insert_case5
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                self.right_rotate(node.parent.parent)
                return

            # symetry
            elif node.parent == node.parent.parent.right:
                node_uncle = node.parent.parent.left
                if node_uncle and node_uncle.color == "RED":
                    node.parent.color = "BLACK"
                    node_uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                    continue
                elif node == node.parent.left:
                    self.right_rotate(node)
                    node = node.right
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                self.left_rotate(node.parent.parent)
                return

        # keep root color black!
        self.root.color = "BLACK"


if __name__ == '__main__':
    element_list = list(np.random.choice(list(range(100)), 15))
    rb_tree = RBTree(element_list)