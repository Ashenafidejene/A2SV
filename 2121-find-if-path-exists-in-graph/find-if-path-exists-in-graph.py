class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i : [] for i in range(n)}
        for first , second in  edges :
            graph[first].append(second)
            graph[second].append(first)
        visit = set()
        def dfs(vertex):
            if vertex == destination:
                return True 
            visit.add(vertex)
            for negibour in graph[vertex]:
                if not ( negibour in visit):
                   find = dfs(negibour)
                   if find:
                       return True 
            return False 
        return dfs(source)