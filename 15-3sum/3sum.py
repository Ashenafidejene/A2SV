class Solution:
    def threeSum(self, nums):
        nums.sort()
        length = len(nums)
        answerset = set()
        answer = []
        for i in range(length -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            b,e = i+1 , length-1
            while b < e :
                sums = nums[i]+nums[b]+nums[e]
                if sums > 0:
                    e-=1
                elif sums < 0:
                    b+=1
                else:
                    answer.append([nums[i],nums[b],nums[e]])
                    b+=1
                    e-=1
                    while b < e and nums[b] == nums[b - 1]:
                        b += 1
                    while b < e and nums[e] == nums[e + 1]:
                        e -= 1
                
        return answer 