'''
Find a number in a sorted 2D matrix

leetcode 74
leetcode 240
'''

import numpy as np

def solution1(matrix, target):
    '''
        :param matrix: The matrix for searching
        :param target: The target to search
        :return: True if the matrix contains the target, False if not
    '''
    if not matrix:
        return False

    # narrow the searching colonms
    for i in range(len(matrix[0]) - 1, -1, -1):
        if matrix[0][i] <= target:
            for j in range(len(matrix)):
                if matrix[j][i] >= target:

                    smaller_matrix = matrix[j:][:i+1]
                    print(smaller_matrix)
                    for x in smaller_matrix:
                        for xy in x:
                            if xy == target:
                                return True
            return False
        else:
            continue

    return False

# sth wrong
# # using the diagonal
# def solution2(matrix, target):
#     '''
#     :param matrix: The matrix for searching
#     :param target: The target to search
#     :return: True if the matrix contains the target, False if not
#     '''
#     row_length = len(matrix)
#     if not row_length:
#         return False
#
#     colomn_length = len(matrix[0])
#     if not colomn_length:
#         return False
#
#     if matrix[-1][-1] < target:
#         return False
#
#     while row_length and colomn_length:
#         row_length -= 1
#         colomn_length -= 1
#
#         if matrix[row_length][colomn_length] == target:
#             return True
#
#         elif matrix[row_length][colomn_length] < target:
#             for index in range(colomn_length, -1, -1):
#                 if matrix[row_length + 1][index] == target:
#                     return True
#             for index in range(row_length, -1, -1):
#                 if matrix[index][colomn_length+1] == target:
#                     return True
#
#             return False
#
#     if row_length or colomn_length:
#         if row_length:
#             smaller_matrix = matrix[:row_length+1]
#         else:
#             smaller_matrix = matrix[:][:colomn_length+1]
#
#         for x in smaller_matrix:
#             for xy in x:
#                 if xy == target:
#                     return True
#
#     return False

# binary search
def solution3(matrix, target):
    if not matrix:
        return False
    if not matrix[0]:
        return False

    height, width = len(matrix), len(matrix[0])
    low, high = 0, height
    while low < high:
        mid = (low + high) // 2
        val = matrix[mid // width][mid % width]
        if val == target:
            return True
        elif val > target:
            high = mid
        else:
            low = mid + 1

    return False


if __name__ == '__main__':
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    print(matrix)
    result = solution1(matrix, target=3)
    print(result)
    # result = solution2(matrix, target=3)
    # print(result)

    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    print(matrix)
    result = solution1(matrix, target=13)
    print(result)
    # result = solution2(matrix, target=13)
    # print(result)

    matrix = [
        [1]
    ]
    print(matrix)
    result = solution1(matrix, target=1)
    print(result)
    # result = solution2(matrix, target=1)
    # print(result)

    matrix = [
        [1]
    ]
    print(matrix)
    result = solution1(matrix, target=2)
    print(result)
    # result = solution2(matrix, target=2)
    # print(result)

    matrix = [
        [1, 3]
    ]
    print(matrix)
    result = solution1(matrix, target=1)
    print(result)
    # result = solution2(matrix, target=1)
    # print(result)

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(matrix)
    result = solution1(matrix, target=7)
    print(result)
    # result = solution2(matrix, target=7)
    # print(result)