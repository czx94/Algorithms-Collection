class Solution(object):
    def maxProfit1(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1 or k < 1:
            return 0

        if k >= len(prices) // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        buys = [prices[0]] * k
        sells = [0] * k
        for price in prices:
            buys[0] = min(buys[0], price)
            sells[0] = max(sells[0], price - buys[0])
            for i in range(1, k):
                buys[i] = min(buys[i], price - sells[i - 1])
                sells[i] = max(sells[i], price - buys[i])

        return sells[-1]

    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1 or k < 1:
            return 0

        if k >= len(prices) // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        profits = [0] * len(prices)
        diff = [x - y for (x, y) in zip(prices[1:], prices[:-1])]
        for _ in range(k):
            prev_profit = 0
            for i in range(1, len(prices)):
                profit = diff[i - 1]
                prev_profit = max(prev_profit + profit, profits[i])
                profits[i] = max(prev_profit, profits[i - 1])

        return profits[-1]
