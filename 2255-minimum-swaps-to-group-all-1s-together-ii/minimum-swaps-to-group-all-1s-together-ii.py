class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        num1 = sum(nums)  
        N = len(nums)     
        extended_nums = nums + nums
        
        cur = minSwap = num1 - sum(extended_nums[:num1])
        
        for i in range(num1, 2 * N):
            cur += extended_nums[i - num1] - extended_nums[i]
            minSwap = min(minSwap, cur)
        
        return minSwap
