class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        sum = [0]
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node, parent):
            total_time = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    time_from_child = dfs(neighbor, node)
                    if time_from_child > 0 or hasApple[neighbor]:
                        total_time += time_from_child + 2
            return total_time
        
        return dfs(0, -1)


            
            