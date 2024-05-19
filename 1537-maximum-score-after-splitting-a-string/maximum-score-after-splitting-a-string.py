class Solution:
    def maxScore(self, s: str) -> int:
        zeroSum = [0] * len(s)
        sumZero = 0
        oneSum = [0] * len(s)
        sumOne = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                sumZero += 1
            zeroSum[i] = sumZero
            
            if s[len(s) - 1 - i] == '1':
                sumOne += 1
            oneSum[len(s) - 1 - i] = sumOne

        maxs = 0
        
        for i in range(len(s) - 1):  # Iterate only up to len(s) - 1
            maxs = max(maxs, zeroSum[i] + oneSum[i + 1])
        
        return maxs