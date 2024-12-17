class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        maxs = float('inf') 
        l = len(nums)-1
        res=0
        for i in range(len(nums)-2):
            b,e = i+1,l
            while b < e : 
                c_res = nums[i]+nums[b]+nums[e]
                if abs(c_res - target) < abs(maxs) :
                    res = c_res 
                    maxs = c_res - target;
                if c_res < target:
                    b+=1
                else:
                    e-=1
        return res 