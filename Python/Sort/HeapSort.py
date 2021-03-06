import numpy as np
import math

class MaxHeap(object):
    def __init__(self, list_object):
        self.heap = list_object
        self.build_max_heap()

    def heap_sort(self, list_object):
        pass

    def max_heapify(self, i):
        left_index = self.left(i)
        right_index = self.right(i)

        if left_index <= len(self.heap) and self.heap[left_index-1] > self.heap[i-1]:
            largest_index = left_index
        else:
            largest_index = i

        if right_index <= len(self.heap) and self.heap[right_index-1] > self.heap[largest_index-1]:
            largest_index = right_index

        if largest_index != i:
            self.heap[i-1], self.heap[largest_index-1] = self.heap[largest_index-1], self.heap[i-1]
            self.max_heapify(largest_index)

    def build_max_heap(self):
        size = len(self.heap)
        for i in range(math.floor(size/2), 0, -1):
            self.max_heapify(i)

    # index for the left subtree of current node
    def left(self, i):
        return 2*i

    # index for the right subtree of current node
    def right(self, i):
        return 2*i+1

    # index for the parent of current node
    def parent(self, i):
        return math.floor(i/2)


    def show_heap(self):
        print(self.heap)
        size = len(self.heap)
        depth = len(bin(size)[2:])

        self.tree_map = [['  ' for _ in range(2**depth-1)] for i in range(depth)]

        self.draw_sub_element(1, list(range(1,2**depth)))

        for layer in self.tree_map:
            print(''.join(layer))

    def draw_sub_element(self, i, index_list):
        if i > len(self.heap) or index_list == []:
            return

        layer = len(bin(i)[2:])-1

        split = int(np.median(index_list))

        self.tree_map[layer][split-1] = str(self.heap[i-1])

        left = self.left(i)
        right = self.right(i)

        self.draw_sub_element(left, index_list[:index_list.index(split)])
        self.draw_sub_element(right, index_list[index_list.index(split)+1:])

    def add_element(self, value):
        self.heap.append(value)
        self.build_max_heap()
        self.show_heap()


if __name__ == '__main__':
    list_object = list(np.random.choice(list(range(10,100)), size=36, replace=False))
    my_heap = MaxHeap(list_object)
    my_heap.show_heap()

    my_heap.add_element(11)