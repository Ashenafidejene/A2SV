class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = {}
        left = 0 
        res = 0
    
        for right in range(len(nums)) : 
            count[nums[right]] = 1 + count.get(nums[right],0)
            while ((right-left+1)- count.get(1,0)) > 1 :
                count[nums[left]] -=1
                left +=1 
            res = max(res, right-left + 1)
        return res-1 if res !=0 else len(nums) - 1 