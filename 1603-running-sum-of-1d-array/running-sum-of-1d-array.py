class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        store =  0 
        for ind in range ( len(nums)) :
            store += nums[ind]
            nums[ind] = store 
        return nums 

