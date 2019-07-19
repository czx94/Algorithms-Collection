from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y: x ^ y, nums)

        count = 0
        while not (xor >> count) & 1:
            count += 1

        first = []
        second = []
        for num in nums:
            if (num >> count) & 1:
                first.append(num)
            else:
                second.append(num)

        first = reduce(lambda x, y: x ^ y, first)
        second = reduce(lambda x, y: x ^ y, second)

        return [first, second]