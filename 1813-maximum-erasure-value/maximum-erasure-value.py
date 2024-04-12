class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        total = 0
        maxs = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                total -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            total += nums[right]
            maxs = max(maxs, total)
        return maxs