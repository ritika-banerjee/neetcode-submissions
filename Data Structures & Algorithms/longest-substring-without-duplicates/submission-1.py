class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        max_len = 0


        while left < len(s):
            seen = set()
            count = 0
            
            while right < len(s)  and  s[right] not in seen:
                seen.add(s[right])
                count += 1
                right += 1
            
            max_len = max(max_len, count)
            left += 1
            right = left


        return max_len