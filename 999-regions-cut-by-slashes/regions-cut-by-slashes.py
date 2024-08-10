class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        r, c = len(grid), len(grid[0])
        r1, c1 = 3 * r, 3 * c
        grid2 = [[0] * c1 for _ in range(r1)]
        
        for i in range(r):
            for j in range(c):
                r2, c2 = i * 3, j * 3
                if grid[i][j] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[i][j] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= r1 or j >= c1 or grid2[i][j] != 0 or (i, j) in visit:
                return
            visit.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        res = 0
        for k in range(r1):
            for j in range(c1):
                if grid2[k][j] == 0 and (k, j) not in visit:
                    dfs(k, j)
                    res += 1
        
        return res