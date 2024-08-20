class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        
        def dfs(start, end, value, visited):
            if start == end:
                return value
            visited.add(start)
            for neighbor, weight in graph.get(start, []):
                if neighbor not in visited:
                    result = dfs(neighbor, end, value * weight, visited)
                    if result != -1:
                        return result
            return -1
        
        
        ans = []
        for x1, x2 in queries:
            if x1 in graph and x2 in graph:
                ans.append(dfs(x1, x2, 1, set()))
            else:
                ans.append(-1.0)
        
        return ans
