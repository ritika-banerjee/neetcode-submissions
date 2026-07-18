class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        right = 0
        freq = {}
        max_len = 0
        max_freq = 0

        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1

            else:
                freq[s[right]] += 1
                
            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len