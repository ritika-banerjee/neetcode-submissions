class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        max_len = 0
        freq = {}
        max_freq = 0

        while right < len(s):
            if s[right] in freq:
               freq[s[right]] += 1

            else:
                freq[s[right]] = 1

            win_length = right - left + 1
            max_freq = max(max_freq, freq[s[right]])
            replacements = win_length - max_freq

            while replacements > k:
                replacements -= 1
                freq[s[left]] -= 1
                left += 1

            win_length = right - left + 1
            max_len = max(max_len, win_length)


            right += 1


        return max_len 