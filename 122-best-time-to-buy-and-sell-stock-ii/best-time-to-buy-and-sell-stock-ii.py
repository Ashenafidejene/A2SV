class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dp(i,flag):
            if i >= len(prices):
                return 0
            value1 = dp(i+1,flag)
            value2 = 0 
            if flag :
                value2 = -prices[i]+dp(i+1,False)
            else:
                value2 = prices[i] + dp(i+1,True)
            return max(value2,value1)
        return dp(0,True)