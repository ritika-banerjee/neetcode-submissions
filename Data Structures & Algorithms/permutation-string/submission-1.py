from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = 0
        target = Counter(s1)
        window = Counter()

        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 == len(s1):
                if target == window:
                    return True
                
                else:
                    window[s2[left]] -= 1
                    left += 1


        return False
