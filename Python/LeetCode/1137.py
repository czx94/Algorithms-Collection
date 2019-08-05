class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            prev_prev, prev, this = 0, 1, 1
            for i in range(2, n):
                prev_prev, prev, this = prev, this, prev_prev + prev + this
            return this