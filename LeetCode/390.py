class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return  1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))