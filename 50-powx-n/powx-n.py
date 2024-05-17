class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the edge case of n being INT_MIN to avoid overflow when negating it
        if n == -2**31:
            x = 1 / x
            n = 2**31 - 1
            return self.myPow(x, n) * x

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result