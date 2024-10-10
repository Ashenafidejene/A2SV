class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxr = [0] * len(nums)
        i = len(nums) - 1
        prev = 0
        
        # Fill maxr with the maximum elements from the right
        for n in reversed(nums):
            maxr[i] = max(n, prev)
            prev = maxr[i]
            i -= 1
            
        res = 0
        l = 0
        
        # Find the maximum width ramp
        for r in range(len(nums)):
            while l < len(nums) and nums[l] > maxr[r]:
                l += 1
            if l < len(nums):
                res = max(res, r - l)
                
        return res