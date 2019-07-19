import numpy as np

def selection_sort(list_object):
    assert len(list_object) >= 1
    for i in range(len(list_object)):
        for j in range(i, len(list_object)):
            if list_object[j] < list_object[i]:
                list_object[i], list_object[j] = list_object[j], list_object[i]

    return list_object

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    sorted_object = selection_sort(list_object)
    print(sorted_object)