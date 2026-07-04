class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        max_p, max_s = 0, 0

        water = [0] * len(height)

        for i in range(1, len(height)):
            max_p = max(max_p, height[i - 1])
            prefix[i] = max_p

        for i in range(len(height) - 2, 0, -1):
            max_s = max(max_s, height[i + 1])
            suffix[i] = max_s
        
        total = 0
        for i in range(len(height)):
            curr = max(0, min(prefix[i], suffix[i]) - height[i])
            total += curr

        return total