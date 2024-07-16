class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arraysum = sum(nums)
        Tsum = 0
        for i in range(0,len(nums)+1):
            Tsum +=i 
        return Tsum - arraysum
