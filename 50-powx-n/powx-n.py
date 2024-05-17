class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Recursive helper function
        def pow_recursive(x, n):
            if n == 0:
                return 1
            half = pow_recursive(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        return pow_recursive(x, n)