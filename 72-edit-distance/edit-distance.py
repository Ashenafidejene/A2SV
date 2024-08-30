class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        memo = {}
        def dp(i, j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            elif i >= len(word1):
               memo[(i,j)]= len(word2) - j
            elif j >= len(word2):
                memo[(i,j)]= len(word1) - i
            elif word1[i] == word2[j]:
                memo[(i,j)]=dp(i + 1, j + 1)
            else:
                memo[(i,j)]= 1 + min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))
            return memo[(i,j)]
        
        return dp(0, 0)