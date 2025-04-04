class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        visit = set()
        for i in range(len(nums)):
            while i+1 != nums[i]:
                if nums[i] == nums[nums[i]-1]:
                    if not(nums[i] in visit) : 
                       ans.append(nums[i])
                       visit.add(nums[i])
                    break 
                temp = nums[i]-1
                nums[i],nums[temp] = nums[temp],nums[i]
        print(nums)
        return ans
  