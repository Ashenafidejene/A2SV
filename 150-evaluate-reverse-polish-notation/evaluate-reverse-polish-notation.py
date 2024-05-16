class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "-/+*"
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Ensure integer division
                    stack.append(int(num1 / num2))
        
        return stack.pop()