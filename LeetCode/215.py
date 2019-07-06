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

    # heap sort
    def findKthLargest4(self, nums, k):
        self.nums = nums
        self.build_max_heap()

        result = []
        for i in range(k):
            nums[0], nums[-1] = nums[-1], nums[0]
            result.append(nums.pop())
            self.max_heapify(1)

        return result[-1]

    def build_max_heap(self):
        for i in range(len(self.nums) // 2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, n):
        left = self.left(n)
        right = self.right(n)

        if left <= len(self.nums) and self.nums[n - 1] < self.nums[left - 1]:
            max_index = left
        else:
            max_index = n

        if right <= len(self.nums) and self.nums[max_index - 1] < self.nums[right - 1]:
            max_index = right

        if max_index != n:
            self.nums[max_index - 1], self.nums[n - 1] = self.nums[n - 1], self.nums[max_index - 1]
            self.max_heapify(max_index)

    def left(self, n):
        return 2 * n

    def right(self, n):
        return 2 * n + 1

    def parent(self, n):
        return n // 2


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