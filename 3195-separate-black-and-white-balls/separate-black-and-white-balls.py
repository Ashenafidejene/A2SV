class Solution:
    def minimumSteps(self, s: str) -> int:
        i=0
        j=0
        count = 0 
        while j < len(s):
            if s[j]=='0':
               count+=(j-i)
               i+=1
            j+=1
        return count 
