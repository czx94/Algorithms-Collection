'''
Find a number in a sorted 2D array
'''

import numpy as np

def solution1(array, target):
    '''
        :param array: The array for searching
        :param target: The target to search
        :return: True if the array contains the target, False if not
    '''
    # narrow the searching colonms
    print('Target is {}'.format(target))
    for i in range(len(array[0]) - 1, -1, -1):
        if array[0][i] < target:
            for j in range(len(array[:,0])):
                if array[j][i] >= target:
                    smaller_array = array[j:, :i+1]

                    print(smaller_array)
                    for x in smaller_array:
                        for xy in x:
                            if xy == target:
                                return True
            return False
        else:
            continue

    return False

# using the diagonal
def solution2(array, target):
    '''
    :param array: The array for searching
    :param target: The target to search
    :return: True if the array contains the target, False if not
    '''
    print('Target is {}'.format(target))
    row_length = len(array)
    colomn_length = len(array[0])

    while row_length and colomn_length:
        row_length -= 1
        colomn_length -= 1

        if array[row_length][colomn_length] == target:
            print(array[:row_length+1, :colomn_length+1])
            return True

        elif array[row_length][colomn_length] < target:
            potential = np.concatenate((array[row_length + 1, :colomn_length+1], array[:row_length+1, colomn_length+1]))
            print(potential)

            for p in potential:
                if p == target:
                    return True
                else:
                    return False

    return False

if __name__ == '__main__':
    array = np.random.randint(0, 100, size=[5,6])
    array.sort(axis=0)
    array.sort(axis=1)
    print(array)
    result = solution2(array, target=array[1][3])
    print(result)