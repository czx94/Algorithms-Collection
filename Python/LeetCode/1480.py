class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        for num in nums:
            if result:
                result.append(result[-1] + num)
            else:
                result.append(num)

        return result