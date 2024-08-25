class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        
        def dp(i, noTrans, holding):
            if i >= len(prices) or noTrans >= k:  
                return 0
            
            if (i, holding, noTrans) in memo:
                return memo[(i, holding, noTrans)]
            
           
            value = dp(i + 1, noTrans, holding)
            
            if holding:
                value2 = prices[i] + dp(i + 1, noTrans + 1, False)
            else:
                value2 = -prices[i] + dp(i + 1, noTrans, True)
            
            memo[(i, holding, noTrans)] = max(value, value2)
            return memo[(i, holding, noTrans)]
        
        return dp(0, 0, False)