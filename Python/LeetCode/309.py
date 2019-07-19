class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        nothing, hold, cooldown = 0, -float('inf'), -float('inf')

        for price in prices:
            nothing, hold, cooldown = max(nothing, cooldown), max(hold, nothing - price), hold + price

        return max(nothing, cooldown)