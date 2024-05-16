class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s : 
            if stack1 and i =='#':
                stack1.pop()
            elif  i =='#' :
                 continue 
            else :
                stack1.append(i)
        for k in t :
            if stack2 and k == '#':
                stack2.pop()
            elif  k =='#' :
                continue 
            else:
                stack2.append(k)
        return stack2 == stack1