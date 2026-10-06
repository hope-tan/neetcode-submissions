class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0;

        # left and right ptr
        buy = 0 # buy price
        sell = 1 # sell price

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            sell += 1
        return maxProfit

        