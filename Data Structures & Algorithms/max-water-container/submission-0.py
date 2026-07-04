class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start, end = 0, len(heights) - 1
        max_area = 0

        while start < end:
            h = min(heights[start], heights[end])
            l = end - start
            area = h * l

            max_area = max(area, max_area)

            if heights[start] < heights[end]:
                start += 1

            else:
                end -= 1

        return max_area