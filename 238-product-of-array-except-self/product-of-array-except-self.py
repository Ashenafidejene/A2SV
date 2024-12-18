class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prifixPro=[1]*len(nums)
        postfixPro=[1]*len(nums)
        prifixPro[0]=nums[0]
        postfixPro[-1]=nums[-1]
        for i in range(1,len(nums)):
            prifixPro[i]*=nums[i]*prifixPro[i-1]
            postfixPro[len(nums)-i-1]*=nums[len(nums)-i-1]*postfixPro[len(nums)-i]
        #print( prifixPro)
        #print( postfixPro)
        #return postfixPro
        
        ans = [postfixPro[1]]
        for j in range(1,len(nums)-1):
            ans.append(postfixPro[j+1]*prifixPro[j-1])
        ans.append(prifixPro[-2])
        return ans
            


            
