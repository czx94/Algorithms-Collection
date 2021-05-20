class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        print(nums)
        for i in range(1, len(nums)+1):
            if i <= nums[i - 1] and (i == len(nums) or i > nums[i]):
                return i

        return -1

if __name__ == '__main__':
    solution = Solution()
    cases = [[3, 5], [0, 0], [0,4,3,0,4], [3,6,7,7,0]]
    for case in cases:
        print(solution.specialArray(case))
