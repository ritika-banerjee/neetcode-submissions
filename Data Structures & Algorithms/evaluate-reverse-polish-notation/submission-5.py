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
                    answer = left + right
                    stack.append(answer)

                elif token == "-":
                    answer = left - right
                    stack.append(answer)

                elif token == "*":
                    answer = left * right
                    stack.append(answer)

                else:
                    answer = int(left / right)
                    stack.append(answer)


        return stack[-1]
