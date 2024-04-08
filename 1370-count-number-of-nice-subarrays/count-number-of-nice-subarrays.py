class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            if k < 0 : return 0 
            res = 0
            left , sum = 0 ,0 
            for right in range(len(nums)):
                if nums[right] % 2 == 1 :
                    sum += 1
                while sum > k:
                    if nums[left] % 2 == 1:
                       sum -= 1
                    left += 1
                res +=(right - left + 1)
            return res 
        return helper(nums, k) - helper(nums, k - 1)


   