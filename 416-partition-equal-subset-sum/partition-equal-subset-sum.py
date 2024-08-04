class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None) 
        def dp(i , target):
            if i >= len(nums) or target <= 0:
                return target == 0
            return dp(i+1,target-nums[i]) or dp(i+1,target)
        return sum(nums) % 2 == 0 and dp(0,sum(nums)//2)