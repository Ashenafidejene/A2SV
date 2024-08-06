class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
       N= len(matrix)
       @lru_cache(None)
       def sums(r,c):
           if r == N:
              return 0 
           if c < 0 or c == N :
              return float('inf')
           return matrix[r][c] + min (sums(r+1,c-1),sums(r+1,c),sums(r+1,c+1))
            
          

       res = float("inf")
       for c in range(N):
           res = min(res,sums(0,c))
       return res 
      