class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while left < right and right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right 
                right += 1
            else:
                max_profit = max(profit, max_profit)
                right += 1
        return max_profit

