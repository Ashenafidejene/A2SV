class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(strs,open,close):
            if open == n and close == n:
                ans.append(strs)
                return 
            #print(strs)
            if open <= n and open > close:
                backtracking(strs+')',open,close+1)
            if open < n :
                backtracking(strs+'(',open+1,close)
        backtracking("",0,0)
        return ans

