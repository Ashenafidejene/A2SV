class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factorization = set()  # Use a set to avoid duplicates

        def facto(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:  # If n is a prime number greater than sqrt(n)
                factorization.add(n)

        for num in nums:
            facto(num)
        
        return len(factorization)