'''
Move all the odd number to the beginning of a list
leetcode 905
'''
import numpy as np

# the simple one, two pointers
def solution1(element_list):
    tail = len(element_list) - 1
    head = 0
    while head < tail:
        while head < tail and element_list[head] & 1:
            head += 1

        while head < tail and element_list[tail] & 1 == 0:
            tail -= 1

        element_list[head], element_list[tail] = element_list[tail], element_list[head]

    return element_list


if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    print(element_list)
    result = solution1(element_list)
    print(result)