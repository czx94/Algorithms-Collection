'''
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                max_len = max(max_len, y - x)
                x += 1

        return max_len


