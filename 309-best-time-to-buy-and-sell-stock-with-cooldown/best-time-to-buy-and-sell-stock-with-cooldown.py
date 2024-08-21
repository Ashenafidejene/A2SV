class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,flag):
            if i >= len(prices):
                return 0
            value1 = dp(i+1, flag)
            if flag:
                value2 = prices[i] + dp(i+2,False)
                return max(value1,value2)
            else:
                value2 = -prices[i]+dp(i+1,True)
                return max(value1,value2)
        return dp(0,False)

            
