'''
Print all the probability of the sum of n dice
'''
import numpy as np

max_value = 6

def solution1(n):
    if n < 1:
        return

    max_sum = n * max_value
    count = np.zeros(max_sum-n+1)
    recursive(n, count)

    total = max_value ** n
    for i in range(n, max_sum+1):
        ratio = count[i-n] / total
        print("%d: %e\n", i, ratio)

def recursive(number, count):
    for i in range(1, max_value+1):
        probability(number, number, i, count)


def probability(original, current, sum, count):
    if current == 1:
        count[sum - original] += 1
    else:
        for i in range(1, max_value+1):
            probability(original, current-1, i + sum, count)


# def solution2(n):
#     if n < 1:
#         return
#
#     max_sum = n * max_value
#     count = [np.ones(max_sum+1), np.zeros(max_sum+1)]
#
#     flag = 0
#
#     for k in range(2, n):
#         for i in range(k):
#             count[1-flag][i] = 0
#
#         for i in range(k, max_value*k+1):
#             count[1-flag][i] = 0
#             j = 1
#             while j <= i and j <= max_value:
#                 count[1-flag][i] += count[flag][i-j]
#                 j += 1
#
#         flag = 1 - flag
#
#     total = max_value ** n
#     for i in range(n, max_sum+1):
#         ratio = count[flag][i] / total
#         print("%d: %e\n", i, ratio)



if __name__ == '__main__':
    print('###solution1###')
    solution1(3)
    print('###solution2###')
    solution2(3)

