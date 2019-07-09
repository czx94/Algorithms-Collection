class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.find_first_k(nums, target), self.find_last_k(nums, target)]

    def find_first_k(self, nums, target):
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1

        return -1

    def find_last_k(self, nums, target):
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                    return mid
                else:
                    head = mid + 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1

        return -1