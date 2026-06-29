class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        hashmap = {}

        for word in strs:
            sorted_chars = sorted(word)
            sorted_chars = "".join(sorted_chars)

            if sorted_chars not in hashmap:
                hashmap[sorted_chars] = [word]

            else: 
                hashmap[sorted_chars].append(word)

        anagrams = [anagram for anagram in hashmap.values()]
        return anagrams