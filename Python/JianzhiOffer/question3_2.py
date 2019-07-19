'''
Find the repeated numbers in a list

List l has a length of n, all its elements are integers between 0 and n - 1.
Some of the elements are repeated, but we don't know how many of them are and for how many times
Objective is to find any of the repeated numbers
The original list cannot be editted
'''
import numpy as np

def solution1(array):
    def count_range(array, head, tail):
        if not array:
            return 0

        count = 0
        for i in range(len(array)):
            if array[i] >= head and array[i] <= tail:
                count += 1

        return count

    array = sorted(array)

    head = 0
    tail = len(array) - 1

    while tail >= head:
        mid = ((tail - head) >> 1) + head
        count = count_range(array, head, mid)

        if tail == head:
            if count > 1:
                return head
            else:
                break

        if count > (mid - head + 1):
            tail = mid
        else:
            head = mid + 1

    return -1

if __name__ == '__main__':
    array = list(np.random.choice(list(range(20)), 20))
    print(array)
    print(solution1(array))
