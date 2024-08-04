class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        MOD = 10**9 + 7
        for j in range(len(nums)):
            temp = nums[j]
            ans.append(temp)
            for i in range(j+1,len(nums)):
                temp += nums[i]
                ans.append(temp)
        ans.sort()
        return sum(ans[left-1:right])%MOD

