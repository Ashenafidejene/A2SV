class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(par,cur):
            if len(ans) == n or cur>n or cur >=(par+1)*10 :
                return
            ans.append(cur)
            dfs(cur,cur*10)
            dfs(par,cur+1)
        dfs(0,1)
        return ans