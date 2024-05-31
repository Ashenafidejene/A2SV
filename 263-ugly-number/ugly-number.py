class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def ugly(n):
            if n == 1:
                return True
            elif n % 5 == 0:
                return ugly(n // 5)
            elif n % 3 == 0:
                return ugly(n // 3)
            elif n % 2 == 0:
                return ugly(n // 2)
            else:
                return False
        return ugly(n)