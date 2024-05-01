class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prifixSum = [0]*len(nums)
        acumulator = 0 
        acumulator1 = 0 
        postFixSum = [0]*len(nums)
        for i in range(len(nums)):
            acumulator += nums[i]
            prifixSum[i] = acumulator
            acumulator1 += nums[len(nums)-1-i]
            postFixSum[len(nums)-1-i] = acumulator1
        for i in range(len(postFixSum )):
            if postFixSum[i] == prifixSum[i]:
                return i
        return -1
            