class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row , col = len(grid) - 1, len(grid[0]) - 1

        def handler(i, j):
            if i < row and j < col:
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
            elif i < row:
                grid[i][j] += grid[i+1][j]
            elif j < col:
                grid[i][j] += grid[i][j+1]

        for i in range(row, -1, -1):
            for j in range(col, -1, -1):
                handler(i, j)

        return grid[0][0]