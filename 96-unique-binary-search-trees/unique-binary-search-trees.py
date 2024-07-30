class Solution:
    def numTrees(self, n: int) -> int:
        return self.factorial(2 * n) // (self.factorial(n + 1) * self.factorial(n))
    
    def factorial(self, n: int) -> int:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial