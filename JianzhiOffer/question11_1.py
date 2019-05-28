'''
Smallest number in a rotated array
'''
import numpy as np

def solution1(array):
    head = 0
    tail = len(array) - 1

    while head < tail - 1:
        mid = (head + tail)//2
        if array[mid] > array[-1]:
            head = mid
        else:
            tail = mid

    return array[tail]

if __name__ == '__main__':
    element_list = sorted(list(np.random.choice(100, size=20, replace=False)))
    n = np.random.randint(10, 15)
    rearranged_element_list = element_list[n:] + element_list[:n]
    smallest = solution1(rearranged_element_list)
    print(rearranged_element_list, smallest, min(rearranged_element_list))
