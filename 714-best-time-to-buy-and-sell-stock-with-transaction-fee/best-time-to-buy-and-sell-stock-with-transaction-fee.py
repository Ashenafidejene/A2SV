class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def dp(i,flag):
            if i >= len(prices):
                return 0
            value1 = dp(i+1,flag)
            value2=0
            if flag:
                value2 = prices[i] + dp(i+1,False)
            else:
                value2 = -prices[i]-fee+dp(i+1,True)
            return max(value1,value2)
        return dp(0,False)