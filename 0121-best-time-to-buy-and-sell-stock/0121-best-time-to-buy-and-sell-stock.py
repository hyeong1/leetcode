class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # buy = 0
        # sell = 1

        # while sell < len(prices):
        #     current_profit = prices[sell] - prices[buy]
        #     if current_profit > 0:
        #         max_profit = max(max_profit, current_profit)
        #     else:
        #         buy = sell
        #     sell += 1
        # return max_profit

        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit