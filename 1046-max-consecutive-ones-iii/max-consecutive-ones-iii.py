class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = {1:0,0:0}
        left = 0 
        res = 0 
        for right in range(len(nums)) : 
            count[nums[right]] += 1
            while ((right-left+1)- count[1]) > k :
                count[nums[left]] -=1
                left +=1 
            res = max(res, right-left + 1)
        return res 