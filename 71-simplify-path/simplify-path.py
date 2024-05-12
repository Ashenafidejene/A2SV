class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        countDot = 0
        for char in path:
            if char == "/":
                if countDot == 2 and len(stack) > 1  :
                    stack.pop()
                    while stack[-1] != '/':
                        stack.pop()
                elif stack[-1] != '/':
                    stack.append(char)
                    countDot = 0
                countDot = 0
            elif char == '.' and stack[-1]=='/':
                countDot += 1
                if countDot == 3:
                    stack.append("...")
                    countDot = 0
            else:
                while countDot!=0:
                    stack.append(".")
                    countDot -= 1
                stack.append(char)   
        if countDot == 2 and len(stack) != 1: 
            stack.pop()
            while stack[-1] != '/':
                stack.pop()
        if stack[-1] == '/' and len(stack) != 1:
            stack.pop()
        return "".join(stack)