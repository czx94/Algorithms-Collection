'''
Given an array nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
'''
class Solution(object):
    # faster than naive one
    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_nums = []
        if k > len(nums) or not nums:
            return max_nums
        if k == 1:
            return nums

        current_window = nums[:k]
        current_max = max(current_window)
        max_nums.append(current_max)
        for i in range(k, len(nums)):
            this_num = nums[i]
            if current_max < this_num:
                current_max = this_num
                current_window.pop(0)
                current_window.append(this_num)

            else:
                current_window.pop(0)
                current_window.append(this_num)
                current_max = max(current_window)

            max_nums.append(current_max)

        return max_nums

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return nums

        index = []
        for i in range(k):
            while index and nums[i] >= nums[index[-1]]:
                index.pop()
            index.append(i)

        max_nums = []
        for i in range(k, len(nums)):
            max_nums.append(nums[index[0]])
            while index and nums[i] >= nums[index[-1]]:
                index.pop()
            if index and index[0] <= i - k:
                index.pop(0)
            index.append(i)

        max_nums.append(nums[index[0]])

        return max_nums


if __name__ == '__main__':
    solution = Solution()
    cases = [([1,3,-1,-3,5,3,6,7],3),([2, 3, 4, 2, 6, 2, 5, 1],3), ([1,-1],1), ([7,2,4],2)]
    for case in cases:
        print(solution.maxSlidingWindow2(*case))
