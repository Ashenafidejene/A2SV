class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LastPro = 1 
        firstPro = 1 
        prifixPro = [1] 
        postFixPro = [1]
        for i in range(len(nums)):
            firstPro *= nums[i]
            LastPro *= nums[len(nums)-1-i]
            prifixPro.append(firstPro)
            postFixPro.insert(0, LastPro)
        for i in range(len(nums)):
            nums[i] =  prifixPro[i] * postFixPro[i+1]
        return nums

            
