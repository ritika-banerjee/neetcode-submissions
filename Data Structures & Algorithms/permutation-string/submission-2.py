from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = 0
        
        target = [0] * 26
        window = [0] * 26

        for s in range(len(s1)):
            index = ord(s1[s]) - ord('a')
            target[index] += 1

        for right in range(len(s2)):
            index = ord(s2[right]) - ord('a')
            window[index] += 1

            if right - left + 1 == len(s1):
                if target == window:
                    return True
                
                else:
                    index = ord(s2[left]) - ord('a')
                    window[index] -= 1
                    left += 1


        return False
