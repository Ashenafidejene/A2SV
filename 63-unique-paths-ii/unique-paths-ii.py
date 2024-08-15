class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        @lru_cache 
        def dp(i , j):
            if i == m-1 and j== n-1:
                return 1
            if obstacleGrid[i][j] == 1:
                return 0 
            ways = 0 
            if i + 1 < m:
                ways += dp(i+1,j)
            if j+1 < n :
                ways += dp(i,j+1)
            return ways 
        return dp(0,0)