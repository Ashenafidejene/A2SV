class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i+1 != nums[i]:
                temp = nums[i]-1
                if nums[i] == nums[temp]:
                    break 
                nums[i],nums[temp] = nums[temp],nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans