class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inital = 0 
        final = len(nums)-1
        middle = (inital + final )//2
        while nums[middle]!=target and final >=inital :
            if nums[middle] == target:
                return 
            if nums[middle] > target:
                final = middle-1               
            else:
                inital= middle+1
            middle = (inital + final )//2
        return middle if nums[middle]==target else -1
