class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V: int = len(graph)
        adj: List[List[int]] = [[] for _ in range(V)]

        # reverse the direction
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)

        # calculate the indegree
        indegree: List[int] = [0] * V

        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1

        # store the node with indegree = 0, in the queue
        queue = deque()

        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        # apply Kahn's alogorithm and store the element in the list
        # basically we are detecting the cycle in the directed graph
        ans: List[int] = []        
        
        while(queue):
            element = queue.popleft()
            ans.append(element)

            for i in adj[element]:
                if indegree[i] != 0:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        # return the sorted list
        return sorted(ans)
