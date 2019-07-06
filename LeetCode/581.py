'''
Given an integer array,
you need to find one continuous subarray that
if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
'''

class Solution(object):
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 2
            else:
                return 0

        head = 0
        tail = len(nums) - 1

        while head < len(nums) - 1 and nums[head] <= nums[head + 1]:
            head += 1

        while tail > 0 and nums[tail - 1] <= nums[tail]:
            tail -= 1

        if tail <= head:
            return 0

        temp = nums[head: tail+1]
        tempMin = min(temp)
        tempMax = max(temp)

        while head > 0 and tempMin < nums[head-1]:
            head -= 1

        while tail < len(nums) - 1 and tempMax > nums[tail+1]:
            tail += 1

        return tail - head + 1


if __name__ == '__main__':
    solution = Solution()
    cases = [[2,6,4,8,10,9,15], [1,2,3,4], [5, 4, 3, 2, 1], [1,3,2,2,2]]
    for case in cases:
        print(solution.findUnsortedSubarray1(case))
