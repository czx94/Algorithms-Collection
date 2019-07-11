class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = 0
        last_max = 0
        i = 0
        jump = 0
        while last_max < len(nums) - 1:
            while i <= last_max:
                current_max = max(i+nums[i], current_max)
                i += 1
            if current_max == last_max:
                return -1
            last_max = current_max
            jump += 1
        return jump