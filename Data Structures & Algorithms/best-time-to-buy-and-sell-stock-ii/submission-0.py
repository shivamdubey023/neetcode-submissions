class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for price in range(1,len(prices)):
            if prices[price] > prices[price-1]:
                total_profit += prices[price] - prices[price-1]

        return total_profit