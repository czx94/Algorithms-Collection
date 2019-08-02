class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = dict()
        for i in range(len(nums)):
            if nums[i] in visited:
                return [i, visited[nums[i]]]
            else:
                visited[target - nums[i]] = i