class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums, goal):
            if goal< 0 : return 0 
            res = 0
            left , sum = 0 ,0 
            for right in range(len(nums)):
                sum += nums[right]
                while sum > goal :
                    sum -= nums[left]
                    left += 1
                res +=(right - left + 1)
            return res 
        return helper(nums, goal) - helper(nums, goal - 1)
