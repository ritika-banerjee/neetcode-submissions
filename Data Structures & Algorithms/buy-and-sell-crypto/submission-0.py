class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_profit = max(max_profit, nums[j] - nums[i])

        return max_profit if max_profit > 0 else 0