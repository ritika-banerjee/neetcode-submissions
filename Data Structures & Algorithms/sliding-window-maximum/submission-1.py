from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        result = []
        dq = deque()

        for right in range(len(nums)):
            if dq and dq[0] < left:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if right - left + 1 == k:
                result.append(nums[dq[0]])
                left += 1

        return result