class Solution(object):
    # this solution is weird
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        maximum = nums[0]
        minimum = nums[0]

        for num in nums[1:]:
            minimum, maximum = min(num, num * maximum, num * minimum), max(num, num * maximum, num * minimum)
            result = max(result, maximum)

        return result

    def maxProduct2(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

if __name__ == '__main__':
    solution = Solution()
    cases = [[2,3,-2,4], [-2,0,-1], [1,2,3,0,2,4]]
    for case in cases:
        print(solution.maxProduct1(case))