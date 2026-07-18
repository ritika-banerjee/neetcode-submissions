class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        if s1 == s2:
            return True

        right = 0
        left = 0
        target = Counter(s1)
        window = Counter()

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            while right - left + 1 > len(s1):
                window[s2[left]] -= 1
                left += 1
                
            if right - left + 1 == len(s1):
                if target == window:
                    return True


        return False