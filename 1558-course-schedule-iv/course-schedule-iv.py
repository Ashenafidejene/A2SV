class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        ans = [set() for _ in range(numCourses)]
        incoming = [0] * numCourses
        
        for pre, cou in prerequisites:
            graph[pre].append(cou)
            incoming[cou] += 1
        
        queue = deque()
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            for neighbor in graph[cur]:
                ans[neighbor].add(cur)
                ans[neighbor].update(ans[cur])
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        lastAnswer = []
        for pre, cou in queries:
            if pre in ans[cou]:
                lastAnswer.append(True)
            else:
                lastAnswer.append(False)
        
        return lastAnswer