class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for s , d in edges :
            graph[s].append(d)
            graph[d].append(s)
        visited = set()
        def dfs(node):
            if node == destination:
                return True 
            visited.add(node)
            for n in graph[node]:
                if n not in visited :
                   found = dfs(n)
                   if found :
                      return True 
            return False 
        return dfs(source)
