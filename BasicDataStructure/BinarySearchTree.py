import numpy as np
from BinaryTree import *

class BST(BinaryTree):
    def __init__(self, elements):
        super.__init__(elements)

    def build_tree(self):
        for element in self.elements:
            self.insert(element)

    def insert(self):
        



