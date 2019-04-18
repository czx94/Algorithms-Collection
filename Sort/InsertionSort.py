import numpy as np

def insertion_sort(list_object):
    assert len(list_object) >= 1
    for i in range(1, len(list_object)):
        value = list_object[i]

        j = i - 1
        while j >= 0 and list_object[j] > value:
            list_object[j + 1] = list_object[j]
            j -= 1

        list_object[j + 1] = value

    return list_object

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=10, replace=False))
    sorted_object = insertion_sort(list_object)
    print(sorted_object)