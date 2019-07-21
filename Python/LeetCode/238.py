class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            return nums[::-1]

        left = [nums[0]]
        right = [nums[-1]]

        for i in range(1, len(nums) - 1):
            left.append(left[-1] * nums[i])
        left = [1] + left

        for i in range(len(nums) - 2, 0, -1):
            right.append(right[-1] * nums[i])
        right.reverse()
        right.append(1)

        products = []
        for i in range(len(nums)):
            products.append(left[i] * right[i])

        return products