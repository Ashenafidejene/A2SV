class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        r,l = 0 , 1
        for RWB in range(3):
            while l < len(nums):
                if nums[r] == RWB:
                    r=r+1
                    l=l+1
                elif nums[l] == RWB:
                    nums[l],nums[r] = nums[r],nums[l]
                else:
                   l = l +1 
            l= r+1
        



