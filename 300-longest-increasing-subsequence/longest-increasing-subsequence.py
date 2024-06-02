class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DynamicArray=[1]*len(nums)
        maxs = 1 
        answer = 1
        for index in range(1,len(nums)):
            for Traverse in range (0,index):
                if nums[Traverse]<nums[index]:
                    maxs= max ( maxs , DynamicArray[Traverse]+1)
            DynamicArray[index] = maxs 
            answer = max ( maxs , answer)
            maxs = 1
        return answer 

        