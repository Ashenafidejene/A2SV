class Solution:
    def divisorGame(self, n: int) -> bool:
        @lru_cache(None)
  
        def dp(num):
            for i in range(1, num):
                if num % i == 0:
                    if not dp(num - i):
                        return True
            return False
        
        return dp(n)
        

               