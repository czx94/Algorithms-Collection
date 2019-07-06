'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_count = dict()
        negative = 0
        for i in range(32):
            bit_count[i] = 0

        for num in nums:
            if num < 0:
                negative += 1
                num *= -1
            bit = 0
            while num:
                if num & 1:
                    bit_count[bit] += 1
                num >>= 1
                bit += 1

        result = 0
        for bit, count in bit_count.items():
            if count % 3:
                result += 2**bit

        if negative % 3 != 0:
            result *= -1
        return result