class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal = len(nums)+1
        left = 0 
        sum = 0
        for right in range(0,len(nums)):
            sum+=nums[right]
            while sum >= target :
                minimal=min(minimal,right-left+1)
                sum-=nums[left]
                left+=1
        return 0 if minimal == len(nums)+1 else minimal
                

                