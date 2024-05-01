class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        accumulator = 0 
        answer = 0 

        for num in nums:
            accumulator += num
            modulus = accumulator % k
            prefixSum[modulus] = prefixSum.get(modulus, 0) + 1

        for index, value in prefixSum.items():  # Changed .values() to .items()
            if index == 0:  # Check if prefix sum is exactly divisible by K
                answer += value * (value + 1) // 2  # Corrected calculation for 0 modulus
            else:
                answer += value * (value - 1) // 2  # Adjusted calculation for other modulus values

        return answer