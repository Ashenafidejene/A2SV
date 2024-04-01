class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(0, int(math.sqrt(c)+1))]
        l , r = 0 , len(nums) - 1 
        while l <= r :
            sum = nums[l]*nums[l] + nums[r]*nums[r]
            if sum > c :
               r-=1
            elif sum < c :
                l += 1
            else :
                return True 
        return False 

        