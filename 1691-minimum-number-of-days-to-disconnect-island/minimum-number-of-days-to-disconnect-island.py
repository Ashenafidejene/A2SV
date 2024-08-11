class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected():
            visited = set()
            
            def dfs(x, y):
                if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x, y) in visited:
                    return
                visited.add((x, y))
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(x + dx, y + dy)
            
            # Find the first land cell to start DFS
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        break
                if visited:
                    break
            
            # Check if all land cells are visited (i.e., one connected component)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        return False
            return len(visited) != 0

        # Check if already disconnected
        if not is_connected():
            return 0
        
        # Check if we can disconnect by changing one cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected():
                        return 1
                    grid[i][j] = 1
        
        # If neither of the above conditions are met, return 2
        return 2