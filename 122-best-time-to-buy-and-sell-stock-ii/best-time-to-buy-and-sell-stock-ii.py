class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,flag):
            if i >= len(prices):
                return 0
            if (i,flag) in memo :
                return memo[(i,flag)]
            value1 = dp(i+1,flag)
            value2 = 0 
            if flag :
                value2 = -prices[i]+dp(i+1,False)
            else:
                value2 = prices[i] + dp(i+1,True)
            memo[(i,flag)]=max(value2,value1)
            return memo[(i,flag)]
        return dp(0,True)