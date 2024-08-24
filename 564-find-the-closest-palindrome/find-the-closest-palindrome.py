class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
    
        # Edge cases for single digit numbers
        if length == 1:
            return str(num - 1)
    
        # Generate the prefix
        prefix = int(n[:(length + 1) // 2])
    
        # Generate possible palindromes
        candidates = set()
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                candidates.add(p + p[::-1])
            else:
                candidates.add(p + p[-2::-1])
    
        # Add edge cases
        candidates.add('9' * (length - 1))
        candidates.add('1' + '0' * (length - 1) + '1')
    
        # Remove the original number itself
        candidates.discard(n)
    
        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
    
        return closest
        