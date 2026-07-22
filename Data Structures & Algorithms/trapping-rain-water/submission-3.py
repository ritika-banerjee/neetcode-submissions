class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        start = 0 
        end = len(height) - 1
        max_left = 0
        max_right = 0

        while start < end:

            max_left = max(max_left, height[start])
            max_right = max(max_right, height[end])

            if max_left < max_right:
                water += max_left - height[start]
                start += 1

            else:
                water += max_right - height[end]
                end -= 1

        return water