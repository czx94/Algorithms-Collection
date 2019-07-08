class Solution(object):
    # only works when a, b are positive
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            xor = a ^ b
            both = (a & b) << 1
            a = xor
            b = both

        return a
