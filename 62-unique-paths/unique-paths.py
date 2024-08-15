class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache
        def dp(i , j):
            if i == m-1 and j== n-1:
                return 1
            ways = 0 
            if i + 1 < m:
                ways += dp(i+1,j)
            if j+1 < n :
                ways += dp(i,j+1)
            return ways 
        return dp(0,0)
