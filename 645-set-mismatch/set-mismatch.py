class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i=0
        while i < n :
            correctPosition = nums[i] - 1
            if correctPosition != i and nums[correctPosition] != correctPosition + 1 :
                nums[correctPosition] , nums[i] = nums[i],nums[correctPosition]
            else:
                i+=1
        for j in range(n):
            if nums[j]-1 != j :
                return[nums[j],j+1]
        return [0,0]
            