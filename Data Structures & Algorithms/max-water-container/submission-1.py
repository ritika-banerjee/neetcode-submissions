class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        max_area = 0

        while start < end:
            left = heights[start]
            right = heights[end]

            height = min(left, right)
            length = end - start 
            area = height * length

            max_area = max(max_area, area)

            if left < right:
                start += 1

            else:
                end -= 1

        return max_area
        
        