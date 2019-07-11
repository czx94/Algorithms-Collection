import copy
class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        current_sum = 0
        max_sum = nums[0]
        element_list = []

        for num in nums:
            element_list.append(num)
            current_sum += num
            if current_sum >= max_sum:
                max_list = copy.copy(element_list)
                max_sum = current_sum

            if current_sum < 0:
                element_list = []
                current_sum = 0

        print(max_list)

        return max_sum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        dp = [0]
        for num in nums:
            dp.append(max(0, dp[-1]) + num)
        dp.pop(0)
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    cases = [[-2,1,-3,4,-1,2,1,-5,4], [-1,-2,-3]]
    for case in cases:
        print(solution.maxSubArray1(case))