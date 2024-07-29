class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph =  [[] for _ in range(n)]
        ans =  [set() for _ in range(n)]
        incoming = [0 for _ in range(n)]
        for i , j in edges:
            graph[i].append(j)
            incoming[j] += 1
        queue = deque()
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.pop()
            for neighbor in graph[cur]:
                ans[neighbor].add(cur)
                ans[neighbor].update(ans[cur])
                incoming [neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        ans = [sorted(list(s)) for s in ans]
        return ans 
        


