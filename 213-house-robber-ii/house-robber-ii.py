class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def dp(i,skips):
            if i >= len(nums):
                return 0 
            if skips and i == len(nums)-1:
                return nums[i] + dp(i+1,skips)
            if i==0:
                return max(nums[i]+dp(i+2,False),dp(i+1,skips))
            if i == len(nums)-1:
                return 0 
            return max(nums[i]+dp(i+2,skips),dp(i+1,skips))
        return dp(0,True)
            
            


            

            

        