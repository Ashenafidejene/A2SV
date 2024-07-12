class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())


          # dic [0:0 1 : 1 2:2 , 3 : 3 4:4] 
                
           



        
        
