class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n + 1)
        dp[0] = 0
        
        for val in range(1, n + 1):
            for i in range(1, int(sqrt(val)) + 1):
                dp[val] = min(dp[val], dp[val - i * i] + 1)
        
        return dp[n]
