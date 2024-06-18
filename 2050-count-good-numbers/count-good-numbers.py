class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 1:
            return 5
        elif n % 2 == 0:
            return pow(5, n // 2, MOD) * pow(4, n // 2, MOD) % MOD
        else:
            return pow(5, n // 2 + 1, MOD) * pow(4, n // 2, MOD) % MOD