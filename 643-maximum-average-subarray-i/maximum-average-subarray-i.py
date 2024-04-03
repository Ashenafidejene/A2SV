class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        maxs= s/k 
        l= 0 
        for m in range (k,len(nums)):
           s-=nums[l]
           s+= nums[m]
           maxs = max(maxs , (s/k))
           l+=1
        return maxs 
        