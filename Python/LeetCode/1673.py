class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = list()
        for i, num in enumerate(nums):
            while result and num < result[-1] and len(result) - 1 + len(nums) - i >= k:
                result.pop()
            if len(result) < k:
                result.append(num)

        return result
