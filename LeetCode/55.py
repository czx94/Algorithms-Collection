class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        max_index = 0
        i = 0
        while i <= max_index:
            if max_index >= len(nums) - 1:
                return True
            max_index = max(max_index, nums[i] + i)
            i += 1

        return False