'''
The k-th smallest numbers
'''
import numpy as np

# sort it
def solution1(nums, k):
    if not nums:
        return

    return sorted(nums)[:k]

def solution2(nums, k):
    if not nums:
        return

    flag = nums[-1]
    left = []
    right = []

    for num in nums[:-1]:
        if num < flag:
            left.append(num)
        else:
            right.append(num)

    if len(left) == k - 1:
        return left + [flag]

    elif len(left) == k:
        return left

    elif len(left) > k:
        return solution2(left, k)

    else:
        return left + [flag] + solution2(right, k - len(left) - 1)


if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    k = 5
    print(element_list, k)
    result = solution1(element_list, k)
    print(result)