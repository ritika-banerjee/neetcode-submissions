class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s == t:
            return t

        if len(s) < len(t):
            return ""

        min_len = float('inf')
        target = Counter(t)
        window = Counter()

        required = len(target)
        formed = 0
        best_left, best_right = 0, 0
        left = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] += 1

            if ch in target and target[ch] == window[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                    best_right = right
                
                ch = s[left]
                if ch in target and target[ch] == window[ch]:
                    formed -= 1
                
                window[ch] -= 1
                if window[ch] == 0:
                    del window[ch]
                left += 1

        if min_len == float('inf'):
            return ""                

        return s[best_left:best_right+1]