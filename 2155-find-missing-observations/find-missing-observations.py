class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
      
        totalSum = mean * (n + len(rolls))
      
        remainSum = totalSum - sum(rolls)
        
      
        if remainSum < n or remainSum > 6 * n:
            return []
        
        
        common = remainSum // n
       
        remain = remainSum % n
        
        
        ans = [common] * n
        
        for i in range(remain):
            ans[i] += 1
        
        return ans


            