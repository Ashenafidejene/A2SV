class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0 or (i, j) in visit:
                return 0
            visit.add((i, j))
            fish_count = grid[i][j]
            # Explore in all four directions
            fish_count += dfs(i + 1, j)
            fish_count += dfs(i - 1, j)
            fish_count += dfs(i, j + 1)
            fish_count += dfs(i, j - 1)
            return fish_count
        
        maximum = 0
        visit = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] != 0:
                    maximum = max(maximum, dfs(i, j))
        
        return maximum
        

            