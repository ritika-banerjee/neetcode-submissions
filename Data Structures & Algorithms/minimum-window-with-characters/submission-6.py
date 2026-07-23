class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter()
        target = Counter(t)

        right, left = 0, 0
        required = len(target)
        formed = 0
        min_len = float('inf')
        best_left = 0
        best_right = 0

        if len(s) < len(t):
            return ""

        if s == t:
            return s

        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in target and window[s[right]] == target[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                    best_right = right

                if s[left] in target and window[s[left]] == target[s[left]]:
                    formed -= 1

                window[s[left]] -= 1
                left += 1

        if min_len == float('inf'):
            return ""

        return s[best_left:best_right+1]            


