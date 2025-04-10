class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i:[] for i in range(1,n+1)}
        for i , j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color = [-1] * n
        result = True
        
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor-1] == -1:
                    color[neighbor-1] = 1 - color[node-1]
                    if not dfs(neighbor):
                        return False
                elif color[neighbor-1] == color[node-1]:
                    return False
            return True
        
        for node in range(1,n+1):
            if color[node-1] == -1:
                color[node-1] = 0
                if not dfs(node):
                    return False
        return True
        