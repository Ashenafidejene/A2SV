class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        queue = deque([0])
        visit.add(0)

        while queue:
            temp = queue.popleft()
            for ech in rooms[temp]:
                if ech  not in  visit:
                     queue.append(ech)
                     visit.add(ech)
        return len(visit) == len(rooms)