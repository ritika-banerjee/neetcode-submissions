class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"

        print(result)
        return result

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0
        while i < (len(s)):
            word = ""
            num = ""
            while s[i] != "#":
                num += s[i]
                i+=1

            i+=1
            l = int(num)
            word = s[i : i+l]
            result.append(word)

            i += l

        return result

