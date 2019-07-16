class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = [[]]
        self.dfs(nums, [])

        return self.results

    def dfs(self, nums, current):
        if not nums:
            return

        for i in range(len(nums)):
            self.results.append(current + [nums[i]])
            self.dfs(nums[:i], current + [nums[i]])