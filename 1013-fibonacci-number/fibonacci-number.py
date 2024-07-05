class Solution:
    def fib(self, n: int) -> int:
        memo = [0,1]
        for  i in range (2,n+1):
            memo.append(memo[i-2] + memo[i-1])
        return memo[n]
   