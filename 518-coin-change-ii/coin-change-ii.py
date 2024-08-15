class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @lru_cache(None)
        def dp(i, amounts):
            if amounts == 0:
                return 1
            if amounts < 0 or i >= len(coins):
                return 0
            return dp(i, amounts - coins[i]) + dp(i + 1, amounts)
        
        return dp(0, amount)