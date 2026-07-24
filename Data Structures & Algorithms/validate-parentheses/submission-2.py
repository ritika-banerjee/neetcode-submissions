class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {
            "}" : "{",
            ")" : "(",
             "]" : "["
        }

        stack = []

        for bracket in s:

            if bracket not in hashmap:
                stack.append(bracket)

            else:
                if not stack:
                    return False
                
                x = stack.pop()
                if x != hashmap[bracket]:
                    return False

        if not stack:
            return True

        return False
