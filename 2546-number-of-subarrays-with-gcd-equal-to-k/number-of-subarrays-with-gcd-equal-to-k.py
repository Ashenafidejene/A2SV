class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        ans = 0
        for i in range(len(nums)):
            current_gcd = nums[i]
            if current_gcd == k:
                ans += 1
            for j in range(i + 1, len(nums)):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    ans += 1
                elif current_gcd < k:
                    break  # No need to continue if GCD is less than k
        return ans

