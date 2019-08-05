'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 0
        length = [0] * len(nums)
        
        
        for num in nums:
            head, tail = 0, size
            while head != tail:
                mid = (head + tail) // 2
                if length[mid] < num:
                    head = mid + 1
                else:
                    tail = mid
            length[head] = num
            size = max(size, head + 1)
            print(length, size)
        return size


if __name__ == '__main__':
    cases = [[10,9,2,5,3,7,101,18], [10,9,2,5,3,4]]
    solution = Solution()
    for case in cases:
        print(solution.lengthOfLIS(case))