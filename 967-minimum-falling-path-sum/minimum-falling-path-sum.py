class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [[0] * N for _ in range(N)]
        
        
        for c in range(N):
            dp[N-1][c] = matrix[N-1][c]
        
     
        for r in range(N-2, -1, -1):
            for c in range(N):
                dp[r][c] = matrix[r][c] + min(
                    dp[r+1][c-1] if c > 0 else float('inf'),
                    dp[r+1][c],
                    dp[r+1][c+1] if c < N-1 else float('inf')
                )
        
       
        return min(dp[0])