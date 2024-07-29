class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for _ in range(len(quiet))]
        ans = list(range(len(quiet)))
        inDegrees = [0]*len(quiet)
        for a , b in richer :
            graph[a].append(b)
            inDegrees[b]+=1
        queue = deque()
        for i in range(0,len(inDegrees)):
            if inDegrees[i] == 0 :
                queue.append(i)
        while queue:
            cur = queue.popleft()  
            for neighbor in graph[cur]:
                if quiet[ans[cur]] < quiet[ans[neighbor]]:
                    ans[neighbor] = ans[cur]
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans


        

            