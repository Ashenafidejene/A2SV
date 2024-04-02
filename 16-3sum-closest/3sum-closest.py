class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j, k = i + 1, n - 1
            if nums[i] + nums[j] + nums[j + 1] >= target:
                k = j + 1
            if nums[i] + nums[k - 1] + nums[k] <= target:
                j = k - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < abs(target - res):
                    res = s
                if s == target:
                    return res
                if s < target:
                    j += 1
                if s > target:
                    k -= 1
        return res
        