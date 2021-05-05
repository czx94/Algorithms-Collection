class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        count0, count1, candidate0, candidate1 = 0, 0, -1, -2
        for num in nums:
            if num == candidate0:
                count0 += 1
            elif num == candidate1:
                count1 += 1
            elif count0 == 0:
                candidate0 = num
                count0 = 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            else:
                count0 -= 1
                count1 -= 1

        return [num for num in [candidate0, candidate1] if nums.count(num) > len(nums) // 3]