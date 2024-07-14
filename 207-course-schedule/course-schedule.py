class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            graph[crs].append(pre)
        visit = set()
        def dfs(node):
            if node in visit:
                return False 
            if graph[node] == []:
                return True 
            visit.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False 
            visit.remove(node)
            graph[node]=[]
            return True 
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True 
