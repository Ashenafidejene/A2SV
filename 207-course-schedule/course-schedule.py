class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph  = {i:[] for i in range(numCourses)}
        for ai  , bi in prerequisites:
            graph[ai].append(bi)
        white = 1 
        gray = 2 
        black = 3 
        color = {i : white for i in range(numCourses)}
        def dfs(node):
            if color[node] == 2 :
                return False
            if color[node] == 1 :
                color[node] = 2 
                for nigbour in graph[node]:
                   if not  dfs(nigbour):
                      return False
                color[node] = 3
            return True 
        for i in range(numCourses):
            #print(i,color)
            if not dfs(i):

                return False
        return True 