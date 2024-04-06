class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , sum= 0 , 0
        minimal = len(nums)+1
        for indx in  range((len(nums))):
            sum +=nums[indx]
            while sum >=target :
                minimal = min(minimal,indx-left+1)
                sum -=nums[left]
                left+=1
        return 0 if minimal == len(nums)+1 else minimal 
                