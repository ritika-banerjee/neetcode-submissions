class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        string_set = set()
        max_count = 0
        
        while right < len(s):
            if s[right] not in string_set:
                string_set.add(s[right])
                right += 1

            else: 
                string_set.remove(s[left])
                left += 1

            max_count = max(right-left, max_count)

        return max_count
