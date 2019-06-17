'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
leetcode 137
'''
import numpy as np

def solution1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return None

    count_dict = dict()

    for s in nums:
        if s not in count_dict:
            count_dict[s] = 1
        else:
            count_dict[s] += 1

    for s in nums:
        if count_dict[s] == 1:
            return s

# bit count, can't solve negative cases
def solution2(nums):
    if not nums:
        return None

    bit_count = {}
    for j in range(32):
        bit_count[j] = 0

    for i in range(len(nums)):
        bit_mask = 1
        for j in range(32):
            bit = nums[i] & bit_mask
            if bit:
                bit_count[j] += 1
            bit_mask <<= 1

    result = 0
    for j in range(32):
        result += (bit_count[j] % 3) << j

    return result

if __name__ == '__main__':
    cases = [[2,2,3,2], [0,1,0,1,0,1,99], [0,2,2,2], [-2,-2,1,1,-3,1,-3,-3,-4,-2]]
    for case in cases:
        result = solution1(case)
        print(result, case)
    for case in cases:
        result = solution2(case)
        print(result, case)


