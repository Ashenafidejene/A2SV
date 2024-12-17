class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = {1:0,0:0}
        maxlength,l,r = 0,0,0

        while r<len(nums):
            count[nums[r]]+=1
            while ((r-l+1)-count[1]>1):
                count[nums[l]]-=1
                l+=1
            maxlength = max(maxlength,(r-l+1))
            r+=1
        return maxlength-1