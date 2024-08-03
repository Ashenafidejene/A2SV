class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(k):
            if k < 3:
                return k 
            if  k not in  memo :
                memo[k] = dp(k-1) + dp(k-2)
            return memo[k]
        return dp(n)


        