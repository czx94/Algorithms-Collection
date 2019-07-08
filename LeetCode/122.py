class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit