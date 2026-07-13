class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for idx, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = idx - i

            stack.append(idx)

        return result
                