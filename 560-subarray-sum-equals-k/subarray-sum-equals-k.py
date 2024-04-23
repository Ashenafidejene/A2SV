
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}  # Initialize a hashmap to store prefix sums and their frequencies
        accumulator = 0
        counter = 0
        
        for num in nums:
            accumulator += num
            # Check if (accumulator - k) exists in the prefixSum hashmap
            if accumulator - k in prefixSum:
                # Increment the counter by the frequency of (accumulator - k)
                counter += prefixSum[accumulator - k]
            # Increment the frequency of accumulator in the prefixSum hashmap
            prefixSum[accumulator] = prefixSum.get(accumulator, 0) + 1
        
        return counter