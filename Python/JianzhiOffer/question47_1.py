'''
Find the max sum of in a route, each time you can just move to the right or to the bottom
leetcode 64
'''
import numpy as np

# dp
def solution1(table):
    value_table = np.zeros(np.array(table).shape)
    if value_table.shape[0] == 1 or value_table.shape[1] == 1:
        return sum(sum(table))

    value_table[0][0] = table[0][0]

    # initialize first column
    for i in range(1, value_table.shape[0]):
        value_table[i][0] = table[i][0] + value_table[i-1][0]

    # initialize first row
    for i in range(1, value_table.shape[1]):
        value_table[0][i] = table[0][i] + value_table[0][i-1]

    # dp for the rest
    for i in range(1, value_table.shape[0]):
        for j in range(1, value_table.shape[1]):
            value_table[i][j] = max(value_table[i-1][j], value_table[i][j-1]) + table[i][j]

    return value_table[-1][-1]

# less storage
def solution2(table):
    table = np.array(table)
    if len(table) == 1 or len(table[0]) == 1:
        return sum((sum(table)))

    value_list = np.zeros(table.shape[1])

    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            up = 0
            left = 0
            if i > 0:
                up = value_list[j]
            if j > 0:
                left = value_list[j-1]

            value_list[j] = max(up, left) + table[i][j]

    return value_list[-1]

if __name__ == '__main__':
    table = [[1, 10, 3, 8],
             [12, 2, 9, 6],
             [5, 7, 4, 11],
             [3, 7, 16, 5]]
    result = solution1(table)
    print(result)
    result = solution2(table)
    print(result)