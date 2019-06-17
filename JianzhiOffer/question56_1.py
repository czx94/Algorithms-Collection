'''
Two elements that appear only one time in a list, other elements appear twice
leetcode 260
'''
from functools import reduce

# seperate the list
def solution1(nums):
    xor = reduce(lambda x, y: x^y, nums)

    bit_count = 0

    while not xor & 1:
        bit_count += 1
        xor >>= 1

    list1 = []
    list2 = []

    for num in nums:
        if (num >> bit_count) & 1:
            list1.append(num)
        else:
            list2.append(num)

    print(list1, list2)
    num1 = reduce(lambda x, y: x^y, list1)
    num2 = reduce(lambda x, y: x^y, list2)
    return [num1, num2]

# same idea using xor
def solution2(nums):
    xor = reduce(lambda x, y: x ^ y, nums)

    mask = 1
    while (xor & mask == 0):
        mask = mask << 1

    num1 = 0
    num2 = 0
    for num in nums:
        if num & mask:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]

if __name__ == '__main__':
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    result = solution1(nums)
    print(result)
    result = solution2(nums)
    print(result)