class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        Tsum = sum(nums)
        lsum = 0
        res = []
        for i , n in enumerate(nums):
            Rsum = Tsum -n - lsum 
            res.append(i*n - lsum + Rsum-(len(nums)-i-1)*n )
            lsum += n 
        return res