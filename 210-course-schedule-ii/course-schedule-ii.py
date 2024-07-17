class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        
        for cou, pre in prerequisites:
            graph[pre].append(cou)
            incoming[cou] += 1
        
        queue = deque()
        order = []
        
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        
        while queue:
            cour = queue.popleft()
            order.append(cour)
            
            for neighbor in graph[cour]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        return order