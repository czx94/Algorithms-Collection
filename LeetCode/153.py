class Solution(object):
    def findMin1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        head = 0
        tail = len(nums) - 1

        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] <= nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[-1]:
                head = mid + 1
            else:
                tail = mid - 1


    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        head = 0
        tail = len(nums) - 1

        while head < tail:
            mid = (head + tail) // 2
            if nums[mid] > nums[-1]:
                head = mid + 1
            else:
                tail = mid

        return nums[tail]
