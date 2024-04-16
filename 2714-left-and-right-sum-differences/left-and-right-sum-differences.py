class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        # Calculate the prefix sum (left sum) array
        left_sum = [0] * n
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
        
        # Calculate the suffix sum (right sum) array
        right_sum = [0] * n
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]
        
        # Calculate the absolute differences between corresponding elements
        answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
        
        return answer
