import numpy as np

def merge_sort(list_object):
    object_number = len(list_object)
    if len(list_object) == 1:
        return list_object
    split_point = object_number//2

    left = merge_sort(list_object[:split_point])
    right = merge_sort(list_object[split_point:])
    list_object = merge(left, right)

    return list_object

def merge(left, right):
    merged_list = list()

    while left and right:
        if left[0] < right[0]:
            value = left.pop(0)
        else:
            value = right.pop(0)

        merged_list.append(value)

    if left:
        merged_list += left
    else:
        merged_list += right

    return merged_list

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    sorted_object = merge_sort(list_object)
    print(sorted_object)