from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        maxMult = 0 
        count = 0 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j)%k==0:
                   count = count + 1  
        return count 
                    