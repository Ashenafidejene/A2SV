class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x, y):
            visited.add((x, y))
           
            for nx, ny in rows[x] + cols[y]:
                if (nx, ny) not in visited:
                    dfs(nx, ny)

        rows = defaultdict(list)
        cols = defaultdict(list)

        
        for x, y in stones:
            rows[x].append((x, y))
            cols[y].append((x, y))

        visited = set()
        num_of_components = 0

        
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                num_of_components += 1

       
        return len(stones) - num_of_components