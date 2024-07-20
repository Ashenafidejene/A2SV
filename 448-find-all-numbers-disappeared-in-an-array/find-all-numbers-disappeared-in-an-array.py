class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i=0
        while i < n :
            correctPosition = nums[i] - 1
            if correctPosition != i and nums[correctPosition] != correctPosition + 1 :
                nums[correctPosition] , nums[i] = nums[i],nums[correctPosition]
            else:
                i+=1
        ans =[]
        for ind in range(n):
            if ind != nums[ind]-1:
                ans.append(ind+1)
        return ans
            
