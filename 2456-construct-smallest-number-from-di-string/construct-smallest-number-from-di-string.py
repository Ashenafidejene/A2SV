class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        for i in range(len(pattern)+1,0,-1):
            stack.append(i)
        ans = ""
        count = 1
        for char in pattern :
            if char == 'I':
                temp = ""
                for i in range(count):
                    temp += str(stack.pop()) 
                ans += temp[::-1]
                count = 1
            else:
                count +=1
        for i in range(0,len(stack)):
            ans += str(stack[i])
        return ans 
            


