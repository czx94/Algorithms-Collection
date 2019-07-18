class Solution(object):
    # general solution for stock
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        s1 = -prices[0]
        s2 = -float('inf')
        s3 = -float('inf')
        s4 = -float('inf')

        for i in range(1, len(prices)):
            # print(s1, -prices[i])
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])
        return max(0, s4)

    def maxProfit2(self, prices):
        if len(prices) <= 1:
            return 0

        profits = []
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            profits.append(max_profit)

        total = 0
        max_profit = 0
        max_price = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total = max(total, max_profit + profits[i])

        return total

    # more clear
    def maxProfit3(self, prices):
        if len(prices) <= 1:
            return 0

        first_buy, second_buy = prices[0], prices[0]
        first_sell, second_sell = 0, 0
        for price in prices:
            first_buy = min(price, first_buy)
            first_sell = max(first_sell, price - first_buy)
            second_buy = min(second_buy, price - first_sell)
            second_sell = max(second_sell, price - second_buy)

        return second_sell

    def maxProfit4(self, prices):
        if len(prices) <= 1:
            return 0

        profits = [0] * len(prices)
        diff = [x - y for (x, y) in zip(prices[1:], prices[:-1])]

        for _ in range(2):
            prev_profit = 0
            for i in range(1, len(prices)):
                profit = diff[i - 1]
                prev_profit = max(prev_profit + profit, profits[i])
                profits[i] = max(prev_profit, profits[i - 1])

        return profits[-1]

if __name__ == '__main__':
    cases = [[3,3,5,0,0,3,1,4], [1,2,3,4,5], []]
    solution = Solution()
    for case in cases:
        print(solution.maxProfit4(case))
