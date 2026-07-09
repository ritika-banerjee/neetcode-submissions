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
            if bracket in hashmap and stack:
                x = stack.pop()
                if hashmap[bracket] != x:
                    return False

            else:
                stack.append(bracket)

        if len(stack) == 0:
            return True

        return False