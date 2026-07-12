class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = 0
        max_len = 0
        numset = set(nums)
        for num in nums:
            if num-1 not in numset:
                current = num
                count = 1
                while current + 1 in numset:
                    count += 1
                    current += 1

            max_len = max(max_len, count)

        return max_len