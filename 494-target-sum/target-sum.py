class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, current_sum):
           
            if i == len(nums):
                return 1 if current_sum == target else 0
            return dp(i + 1, current_sum + nums[i]) + dp(i + 1, current_sum - nums[i])

        return dp(0, 0)