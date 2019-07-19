from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return

        cmp = lambda n1, n2: -int(str(n1) + str(n2)) + int(str(n2) + str(n1))
        array = sorted(nums, key=cmp_to_key(cmp))
        return str(int(''.join([str(i) for i in array])))