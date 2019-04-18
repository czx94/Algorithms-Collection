import numpy as np
import math

class MaxHeap(object):
    def __init__(self, list_object):
        self.heap = list_object
        self.build_max_heap()

    def heap_sort(self, list_object):
        pass

    def max_heapify(self, heap, i):
        left_index = self.left(i)
        right_index = self.right(i)

        if left_index < len(heap) and heap[left_index] > heap[i]:
            largest_index = left_index
        else:
            largest_index = i

        if right_index < len(heap) and heap[right_index] > heap[largest_index]:
            largest_index = right_index

        if largest_index != i:
            heap[i], heap[largest_index] = heap[largest_index], heap[i]
            self.max_heapify(heap, largest_index)


    def build_max_heap(self):
        size = len(self.heap)
        for i in range(math.floor(size/2), -1, -1):
            self.max_heapify(self.heap, i)

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def parent(self, i):
        return math.floor(i/2)

    def show_heap(self):
        print(self.heap)
        # size = len(self.heap)
        # depth = len(bin(size)[2:])
        #
        # self.tree_map = [' ' * (2**depth-1)] * depth
        #
        # self.draw_sub(0, list(range(2**depth-1)))
        #
        # print(self.tree_map)

    # def draw_sub(self, i, index_list):
    #     print(self.tree_map)
    #     if i > len(self.heap) or index_list == []:
    #         return
    #
    #     layer = len(bin(i)[2:])
    #     print(np.median(index_list), index_list)
    #     split = int(np.median(index_list))
    #
    #     self.tree_map[layer] = str(self.heap[i]).join([self.tree_map[layer][:split], self.tree_map[layer][split+1:]])
    #
    #     left = self.left(i)
    #     right = self.right(i)
    #
    #     self.draw_sub(left, index_list[:split])
    #     self.draw_sub(right, index_list[split+1:])


if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=7, replace=False))
    my_heap = MaxHeap(list_object)
    my_heap.show_heap()