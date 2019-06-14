class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = None
        count = 0
        for element in nums:
            if not count:
                number = element
                count = 1
            else:
                if number == element:
                    count += 1
                else:
                    count -= 1

        return number