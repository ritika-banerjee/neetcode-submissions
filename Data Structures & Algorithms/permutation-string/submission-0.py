from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = 0

        for right in range(len(s2)):
            if right - left + 1 == len(s1):
                if Counter(s1) == Counter(s2[left: right + 1]):
                    return True
                
                else:
                    left += 1

            right += 1

        return False
