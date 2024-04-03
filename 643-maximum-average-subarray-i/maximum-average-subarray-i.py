class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum= 0
        maxs = 0
        for i in range(k):
            sum += nums[i]
        maxs= sum/k 
        l= 0 
        for m in range (k,len(nums)):
           sum-=nums[l]
           sum+= nums[m]
           maxs = max(maxs , (sum/k))
           l+=1
        return maxs 
        