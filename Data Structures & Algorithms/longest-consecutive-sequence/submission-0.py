class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        max_seq_len = 0

        for num in nums:
            if num - 1 in numset:
                continue
            
            current = num
            max_length = 1
            while current + 1 in numset:
                max_length += 1
                current += 1
                
            max_seq_len = max(max_seq_len, max_length)

        return max_seq_len