import numpy as np

def bubble_sort1(list_object):
    assert len(list_object) >= 1
    for i in range(1, len(list_object)):
        while i > 0 and list_object[i] < list_object[i-1]:
            list_object[i], list_object[i-1] = list_object[i-1], list_object[i]
            i -= 1

    return list_object

def bubble_sort2(list_object):
    assert len(list_object) >= 1
    for i in range(1, len(list_object)):
        for j in range(len(list_object)-i-1):
            if list_object[i] < list_object[i-1]:
                list_object[i], list_object[i-1] = list_object[i-1], list_object[i]

    return list_object

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    sorted_object = bubble_sort1(list_object)
    print(sorted_object)
    sorted_object = bubble_sort2(list_object)
    print(sorted_object)