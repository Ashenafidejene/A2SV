class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtracing(strs,val,current):
            if len(strs) == 1:
                return val ==int(strs) + current
            if len(strs)==0:
                return val == current

            for index in range(1,len(strs) + 1):
                if val >= int(strs[0:index]) + current:
                   if backtracing(strs[index:],val,int(strs[0:index])+current):
                       return True
                else:
                    return False 
            return False 
        total = 1 
        for i in range(2,n+1):
            strs = str(i*i)

            if backtracing(strs,i,0):
                total += i*i
        return total 

