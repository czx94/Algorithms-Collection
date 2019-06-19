'''
leetcode 121. Best Time to Buy and Sell Stock
leetcode 122 similar
'''

def solution1(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

if __name__ == '__main__':
    tests = [[7,1,5,3,6,4], [7,6,4,3,1]]
    for test in tests:
        print(solution1(test))