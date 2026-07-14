class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0) 
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    left = stack[-1]
                
                else:
                    left = -1

                width = i - left - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area