class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            
            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] == 0:
                return True
            
            
            grid2[x][y] = 0
            
            
            is_sub_island = True
            
           
            if grid1[x][y] == 0:
                is_sub_island = False
            
           
            is_sub_island &= dfs(x + 1, y)
            is_sub_island &= dfs(x - 1, y)
            is_sub_island &= dfs(x, y + 1)
            is_sub_island &= dfs(x, y - 1)
            
            return is_sub_island
        
        m, n = len(grid1), len(grid1[0])
        sub_island_count = 0
        
        for i in range(m):
            for j in range(n):
               
                if grid2[i][j] == 1:
                   
                    if dfs(i, j):
                        sub_island_count += 1
                        
        return sub_island_count      