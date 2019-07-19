'''
Cluster of all sorts
'''
import numpy as np

def bubble_sort(nums):
    if not nums:
        return nums

    for i in range(1, len(nums)):
        while i > 0 and nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1

    return nums

def count_sort(nums):
    if not nums:
        return nums

    count_dict = {}
    new_list = [0] * len(nums)
    lower = min(nums)
    upper = max(nums)

    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num in range(lower, upper):
        count_dict[num + 1] = count_dict.get(num + 1, 0) + count_dict.get(num, 0)

    for num in nums:
        new_list[count_dict[num] - 1] = num
        count_dict[num] -= 1

    return new_list

def insertion_sort(nums):
    if not nums:
        return nums

    for i in range(1, len(nums)):
        value = nums[i]

        i -= 1
        while i >= 0 and nums[i] > value:
            nums[i+1] = nums[i]
            i -= 1

        nums[i+1] = value

    return nums

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    divide = len(nums)//2
    l1 = merge_sort(nums[:divide])
    l2 = merge_sort(nums[divide:])
    return merge(l1, l2)

def merge(l1, l2):
    '''

    :param l1: sorted list1
    :param l2: sorted list2
    :return: sorted list of l1 and l2
    '''
    combined_list = []
    while l1 and l2:
        if l1[0] < l2[0]:
            combined_list.append(l1.pop(0))
        else:
            combined_list.append(l2.pop(0))

    if l2:
        combined_list += l2
    if l1:
        combined_list += l1

    return combined_list

def quick_sort1(nums):
    if not nums:
        return nums

    flag = nums[-1]
    left = []
    right = []
    for num in nums[:-1]:
        if num < flag:
            left.append(num)
        else:
            right.append(num)

    return quick_sort1(left) + [flag] + quick_sort1(right)

def quick_sort2(nums):
    if len(nums) <= 1:
        return nums

    nums, index = partition(nums)
    left = quick_sort2(nums[:index])
    right = quick_sort2(nums[index:])

    return left + right

def partition(nums):
    index = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[-1]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
            
    nums[index], nums[-1] = nums[-1], nums[index]
    return nums, index

def shell_sort(nums):
    if not nums:
        return nums

    step = len(nums)//2
    while step >= 1:
        for i in range(step, len(nums)):
            while i >= step:
                if nums[i] < nums[i - step]:
                    nums[i], nums[i - step] = nums[step], nums[i]
                i -= step
        step //= 2

    return nums

class MaxHeap(object):
    def __init__(self, nums):
        self.nums = nums
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.nums)//2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, n):
        left = self.left(n)
        right = self.right(n)

        if left <= len(self.nums) and self.nums[n-1] < self.nums[left-1]:
            max_index = left
        else:
            max_index = n

        if right <= len(self.nums) and self.nums[max_index-1] < self.nums[right-1]:
            max_index = right

        if max_index != n:
            self.nums[max_index-1], self.nums[n-1] = self.nums[n-1], self.nums[max_index-1]
            self.max_heapify(max_index)

    def left(self, n):
        return 2*n

    def right(self, n):
        return 2*n + 1

    def parent(self, n):
        return n//2


if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    print('######raw############')
    print(list_object)
    sorted_list = bubble_sort(list_object)
    print('######bubble sort##########')
    print(sorted_list)
    sorted_list = count_sort(list_object)
    print('######count sort##########')
    print(sorted_list)
    sorted_list = merge_sort(list_object)
    print('######merge sort##########')
    print(sorted_list)
    sorted_list = quick_sort1(list_object)
    print('######quick sort1##########')
    print(sorted_list)
    sorted_list = quick_sort2(list_object)
    print('######quick sort2##########')
    print(sorted_list)
    sorted_list = insertion_sort(list_object)
    print('######insertion sort##########')
    print(sorted_list)
    sorted_list = shell_sort(list_object)
    print('######shell sort##########')
    print(sorted_list)
