from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        answer = 0
        stack = deque()
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))

            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)

                elif token == "-":
                    stack.append(left - right)

                elif token == "*":
                    stack.append(left * right)

                else:
                    stack.append( int(left / right))


        return stack[-1]
