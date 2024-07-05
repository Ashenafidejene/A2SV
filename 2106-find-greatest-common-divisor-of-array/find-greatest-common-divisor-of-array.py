class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxs = max(nums)
        mins = min(nums)

        def gcd(a,b):
            if b==0 :
                return a 
            return gcd(b,a%b)
        return gcd(maxs,mins)