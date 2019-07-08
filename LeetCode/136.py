from functools import reduce

class Solution:

    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        else:
            flag = nums[-1]
            left = []
            right = []
            for num in nums[:-1]:
                if num <= flag:
                    left.append(num)
                else:
                    right.append(num)
            left = [flag] + left

            if len(left) & 1:
                return self.singleNumber1(left)
            else:
                return self.singleNumber1(right)

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)