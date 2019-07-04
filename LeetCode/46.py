'''
Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []

        self.dfs(nums, [])
        return self.result


    def dfs(self, nums, current):
        if not nums:
            self.result.append(current)

        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], current+[nums[i]])

