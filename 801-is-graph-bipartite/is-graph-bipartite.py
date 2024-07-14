class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        result = True
        
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True
        
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
    