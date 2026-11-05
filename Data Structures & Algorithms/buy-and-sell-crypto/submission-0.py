class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[:i])
            money = max(money,profit)
        return money