'''
Given a list of non negative integers, arrange them such that they form the smallest number.
leetcode 179
'''
from functools import cmp_to_key

def solution1(nums):
    if not nums:
        return

    cmp = lambda n1, n2: int(str(n1)+str(n2)) - int(str(n2)+str(n1))
    array = sorted(nums, key=cmp_to_key(cmp))
    return int(''.join([str(i) for i in array]))

if __name__ == '__main__':
    # nums = [3, 32, 321]
    nums = [0, 0]
    result = solution1(nums)
    print(result)