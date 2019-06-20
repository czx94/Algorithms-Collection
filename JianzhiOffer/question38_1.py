'''
Permutation in String
leetcode 46
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], result)

        return result

    def dfs(self, nums, current, result):
        if not nums:
            result.append(current)

        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], current + [nums[i]], result)