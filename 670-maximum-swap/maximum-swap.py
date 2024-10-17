class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [ i for i in str(num)]
        maxd = '0'
        maxi=swapi=swapj=-1
        for i in reversed(range(len(nums))):
            if nums[i] > maxd:
                maxd=nums[i]
                maxi = i
            if nums[i]<maxd:
                swapi,swapj = i,maxi
        nums[swapi],nums[swapj] = nums[swapj],nums[swapi]
        return int("".join(nums))
