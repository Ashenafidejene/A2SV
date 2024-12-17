class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        m = -1
        count_odds = 0
        ans = 0
        
        for r in range(len(nums)):
           
            if nums[r] % 2:
                count_odds += 1
            
            
            while count_odds > k:
                if nums[l] % 2:
                    count_odds -= 1
                l += 1
            
            
            if count_odds == k:
                if m < l:  
                    m = l
                    while nums[m] % 2 == 0:
                        m += 1
                
               
                ans += m - l + 1
        
        return ans