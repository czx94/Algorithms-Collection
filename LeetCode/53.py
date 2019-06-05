class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        max_sum = nums[0]
        element_list = []
        for num in nums:
            element_list.append(num)
            current_sum = sum(element_list)
            if current_sum < 0:
                element_list = []
            max_sum = max(current_sum, max_sum)

        return max_sum