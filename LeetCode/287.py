class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            while nums[index] != index:
                if nums[index] == nums[nums[index]]:
                    return nums[index]
                else:
                    temp = nums[index]
                    nums[index] = nums[temp]
                    nums[temp] = temp

    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]

        head = 0
        while nums[slow] != nums[head]:
            slow = nums[slow]
            head = nums[head]

        return nums[head]

    def findDuplicate3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                return nums[index]
            index += 1
