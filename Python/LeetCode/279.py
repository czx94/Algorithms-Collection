class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, ]
        for i in range(1, n+1):
            dp.append(min([dp[-j*j] for j in range(1, int(i**0.5)+1)]) + 1)
        return dp[n]