class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 1, 1
        for i in range(n - 1):
            prev, current = current, prev + current

        return current