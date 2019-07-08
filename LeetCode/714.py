class Solution(object):
    # dp
    def maxProfit1(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])

        return cash

    # greedy
    def maxProfit2(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        base = prices[0]
        count = 0

        for i in range(1, len(prices)):
            if prices[i] < base:
                base = prices[i]
            elif prices[i] > base + fee:
                count += prices[i] - base - fee
                base = prices[i] - fee

        return count

if __name__ == '__main__':
    solution = Solution()
    cases = [([1, 3, 2, 8, 4, 9], 2), ([1, 3, 2, 8, 9], 2)]
    for case in cases:
        print(case)
        print(solution.maxProfit2(*case))



