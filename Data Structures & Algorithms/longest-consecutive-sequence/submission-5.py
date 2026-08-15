class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_len = 0

        for i in range(len(nums)):
            current = nums[i]
            
            if current - 1 in seen:
                continue

            length = 1
            while current + 1 in seen:
                length += 1
                current += 1

            max_len = max(length, max_len)

        return max_len

