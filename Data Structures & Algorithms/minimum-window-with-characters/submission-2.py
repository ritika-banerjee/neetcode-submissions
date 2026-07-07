from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        if s == t:
            return s

        counter_t = Counter(t)
        counter_s = Counter()
        min_len = float('inf')
        best_left, best_right = 0, 0

        left = 0
        for right in range(len(s)):
            counter_s[s[right]] += 1

            while counter_s >= counter_t:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                    best_right = right

                counter_s[s[left]] -= 1
                if counter_s[s[left]] == 0:
                    del counter_s[s[left]]
                left += 1

        if min_len == float('inf'):
            return ""

        return s[best_left:best_right + 1]