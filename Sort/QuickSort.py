import numpy as np

'''
This implementation is not in-place
'''

def quick_sort1(list_object):
    if len(list_object) <= 1:
        return list_object

    middle_index, list_object = partition(list_object)
    small = list_object[:middle_index]
    big = list_object[middle_index:]
    small = quick_sort1(small)
    big = quick_sort1(big)
    return small + big

def partition(list_object):
    key = list_object[-1]
    count = 0
    for i in range(len(list_object) - 1):
        if list_object[i] < key:
            list_object[count], list_object[i] = list_object[i], list_object[count]
            count += 1

    list_object[-1], list_object[count] = list_object[count], list_object[-1]
    return count, list_object

def quick_sort2(list_object):
    if len(list_object) <= 1:
        return list_object

    pivot = list_object[-1]

    left = []
    right = []
    for num in list_object[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort2(left) + [pivot] + quick_sort2(right)

def quick_sort_3way(list_object):
    pass

def quick_sort_dual_pivot(list_object):
    pass

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    sorted_list = quick_sort2(list_object)
    print(sorted_list)