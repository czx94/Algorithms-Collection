from functools import reduce
class Solution(object):
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((len(nums)+1)*len(nums)>>1) - sum(nums)

    def missingNumber2(self, nums):
        return reduce(lambda x, y: x^y, nums + range(len(nums) + 1))