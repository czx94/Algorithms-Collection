import numpy as np
from InsertionSort import *

def shell_sort(list_object):
    assert len(list_object) >= 1

    step = len(list_object)//2

    while step >= 1:
        for i in range(step, len(list_object)):
            j = i
            while (j - step) >=0:
                if list_object[j] < list_object[j - step]:
                    list_object[j], list_object[j - step] = list_object[j - step], list_object[j]
                    j -= step
                else:
                    break

        step //= 2

    return list_object

if __name__ == '__main__':
    list_object = list(np.random.choice(100, size=15, replace=True))
    sorted_object = shell_sort(list_object)
    print(sorted_object)