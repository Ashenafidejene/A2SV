class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        i = 0
        while i < len(path):
            if path[i] == '/':
                if stack and  stack[-1]=='/':
                    i+=1
                    continue
                stack.append(path[i])

            elif path[i]=='.':
                j=i+1
                dot = 1
                while j < len(path) and path[j]!='/':
                   
                    if path[j-1]==path[j] and path[j]=='.':
                        dot+=1
                    else:
                        dot=float("inf")
                    j+=1
                if dot == 2 : 
                    if stack:
                        x=stack.pop()
                        if stack:
                           x=stack.pop()
                    i+=2
                    continue
                elif dot==1:
                    i+=1
                    continue
                else:
                    stack.append(path[i:j])
                    i=j
            else:
                k=i
                while k<len(path) and path[k]!='/':
                    k+=1
                stack.append(path[i:k])
                i=k

        if len(stack)==1:
            return stack[-1]
        if stack and stack[-1]=='/':
            stack.pop()
        if len(stack)==0:
            return '/'
        return "".join(stack)