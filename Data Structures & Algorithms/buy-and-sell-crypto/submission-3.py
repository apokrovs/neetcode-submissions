class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for p in range(1,len(prices)):
            buy = min(buy,prices[p])
            max_profit = max(max_profit, prices[p]-buy)
        return max_profit

        