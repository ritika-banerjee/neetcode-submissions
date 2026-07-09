from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        hashmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for bracket in s:

            if bracket not in hashmap:
                stack.append(bracket)

            else:
                if not stack:
                    return False
                    
                x = stack.pop()
                if hashmap[bracket] != x:
                    return False


        if len(stack) == 0:
            return True

        return False