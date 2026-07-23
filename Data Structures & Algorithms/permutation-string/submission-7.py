class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        window = [0] * 26
        left = 0

        for s in s1:
            idx = ord(s) - ord('a')
            target[idx] += 1

        for right in range(len(s2)):
            ch = s2[right]
            idx = ord(ch) - ord('a')

            window[idx] += 1
            if right - left + 1 == len(s1):
                if window == target:
                    return True

                else:
                    ch = s2[left]
                    idx = ord(ch) - ord('a')
                    window[idx] -= 1
                    left += 1

        return False