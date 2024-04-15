class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        left = 0 
        right = k-1
        count = 0 
        for right in range ( k-1,len(nums)):
           print(nums[left:right+1])
           if int(nums[left:right+1])!= 0 and  num % int(nums[left:right+1])==0: 
              count+=1
           left+=1
        return count 


