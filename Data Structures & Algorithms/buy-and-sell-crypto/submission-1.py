class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for num in nums:
            min_price = min(num, min_price)
            max_profit = max(max_profit, num - min_price)

        return max_profit
        