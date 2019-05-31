import numpy as np
from functools import reduce

class Solution(object):
    # count
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # counter = {0:0, 1:0, 2:0}
        # for num in nums:
        #     counter[num] += 1
        #
        # nums = reduce(lambda x, y: x + y, map(lambda x: counter[x]*[x], range(3)))
        # return nums

        counter = {0: 0, 1: 0, 2: 0}
        for num in nums:
            counter[num] += 1

        for i in range(len(nums)):
            if i < counter[0]:
                nums[i] = 0
            elif i < counter[1] + counter[0]:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums

    # pythonic
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return sorted(nums)

    # dynamic count
    def sortColors3(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = len(nums) -1
        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                one += 1
                zero += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1

        return nums

if __name__ == '__main__':
    solution = Solution()
    array = list(np.random.choice(3, size=10))
    print('solution1')
    print(array)
    result = solution.sortColors1(array)
    print(result)


    array = list(np.random.choice(3, size=10))
    print('solution2')
    print(array)
    result = solution.sortColors2(array)
    print(result)

    array = list(np.random.choice(3, size=10))
    print('solution3')
    print(array)
    result = solution.sortColors2(array)
    print(result)