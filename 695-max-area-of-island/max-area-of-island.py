class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0  # Mark the cell as visited
            area = 1  # Count the current cell
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                area += dfs(new_row, new_col)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)
        
        return max_area