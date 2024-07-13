class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for a , b in roads :
            graph[a].add(b)
            graph[b].add(a)
        res = 0 
        for a, b in itertools.combinations(range(n), 2):
            has_connection = 1 if a in graph[b] else 0
            a1 = len(graph[a])
            b1 = len(graph[b])
            res = max (res , a1 + b1 - has_connection )
        return res 
            

