class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v, w in edges:
            if w < 0: continue
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijktras():
            pq = [(0, source)]
            heapq.heapify(pq)
            min_dist = [math.inf] * n
            min_dist[source] = 0

            while pq:
                wei, node = heapq.heappop(pq)
                for v, w in graph[node]:
                    if (wei + w) < min_dist[v]:
                        min_dist[v] = wei + w
                        heapq.heappush(pq, (min_dist[v], v))
            return min_dist[destination]
        
        INF = target + 1
        shrt_dist = dijktras()

        if shrt_dist < target:
            return []

        if shrt_dist == target:
            for i, (u, v, w) in enumerate(edges):
                if w == -1:
                    edges[i][2] = INF
            return edges
        
        for i, (u, v, w) in enumerate(edges):
            if w != -1: continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            new_dist = dijktras()
            if new_dist <= target:
                edges[i][2] += target - new_dist
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []       