class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visit = set()
        ans = []
        def dfs(i,test):
            test.append(i)
            if i == len(graph)-1 :
                ans.append(test)
                return 
            for nigbour in graph[i]:
                dfs(nigbour,test.copy())
        dfs(0,[])
        return ans 

            
