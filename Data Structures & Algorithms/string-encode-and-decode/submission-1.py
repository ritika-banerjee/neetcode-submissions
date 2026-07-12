class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        
        right = 0
        result = []

        while right < len(s):
            length = ""
            while s[right] != "#":
                length += s[right]
                right += 1

            right += 1
            num = int(length)
            result.append(s[right:right+num])

            right += num

        return result