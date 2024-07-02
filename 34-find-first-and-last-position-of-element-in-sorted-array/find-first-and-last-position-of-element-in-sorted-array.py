class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmost(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRightmost(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        leftmost = findLeftmost(nums, target)
        rightmost = findRightmost(nums, target)
        
        # Check if target is actually present in the array
        if leftmost <= rightmost and rightmost < len(nums) and nums[leftmost] == target and nums[rightmost] == target:
            return [leftmost, rightmost]
        else:
            return [-1, -1]
        
        