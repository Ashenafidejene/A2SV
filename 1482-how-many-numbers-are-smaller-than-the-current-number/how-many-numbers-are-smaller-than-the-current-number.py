class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        count2 ={}
        for i in range(len(nums)):
            count[nums[i]]= 1 + count.get(nums[i],0)
        sorted_items = sorted(count.items(), reverse=False)
        sample=0
         #print(sorted_items)
        for key, value in sorted_items:
            count2[key]= sample
            sample +=value
        for k in range(len(nums)):
            nums[k]=count2[nums[k]]
        return nums