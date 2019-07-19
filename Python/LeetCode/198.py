class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, now = 0, 0
        for num in nums:
            print(prev, now)
            prev, now = now, max(num + prev, now)

        return now

if __name__ == '__main__':
    cases = [[1,2,3,1], [2,7,9,3,1]]
    solution = Solution()
    for case in cases:
        print(solution.rob(case))
