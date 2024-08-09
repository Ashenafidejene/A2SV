class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(grid, r, c):
            
            nums = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            if sorted(nums) != list(range(1, 10)):
                return False
            row_sum = [sum(grid[r+i][c+j] for j in range(3)) for i in range(3)]
            col_sum = [sum(grid[r+i][c+j] for i in range(3)) for j in range(3)]
            diag1_sum = sum(grid[r+i][c+i] for i in range(3))
            diag2_sum = sum(grid[r+i][c+2-i] for i in range(3))

            return len(set(row_sum + col_sum + [diag1_sum, diag2_sum])) == 1

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(grid, r, c):
                    count += 1

        return count