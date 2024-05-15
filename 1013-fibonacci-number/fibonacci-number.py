class Solution:
    def fib(self, n: int) -> int:
        def sn(n):
            if n == 0:
                return 0 
            if n == 1:
                return 1 
            return sn(n - 1) + sn(n - 2)
        
        return sn(n)