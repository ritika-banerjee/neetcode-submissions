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

        for i in range(len(height)):
            water[i] = min(prefix[i], suffix[i]) - height[i]

        print(prefix)
        print(suffix)
        print(water)
        total_water = 0
        for w in water:
            if w > 0:
                total_water += w

        return total_water