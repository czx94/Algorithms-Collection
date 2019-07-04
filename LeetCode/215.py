'''
K-th largest number in a list
'''

class Solution(object):
    # O(n), recursive, like merge sort, too slow
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        flag = nums[-1]
        left = []
        right = []

        for num in nums[:-1]:
            if num > flag:
                right.append(num)
            else:
                left.append(num)

        if len(right) == k - 1:
            return flag
        elif len(right) < k - 1:
            return self.findKthLargest1(left, k-len(right)-1)
        else:
            return self.findKthLargest1(right, k)

    # sorted, still slow
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

    # like bubble sort, just make sure the largest elements are well sorted, O(nk)
    def findKthLargest3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums[len(nums)-k]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        # 5
        ([3,2,1,5,6,4], 2),
        # 4
        ([3,2,3,1,2,4,5,5,6], 4)
    ]
    for case in cases:
        nums, k = case
        print(case, solution.findKthLargest4(nums, k))