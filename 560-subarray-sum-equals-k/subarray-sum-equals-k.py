
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prifixSum = {0:1}
        sums = 0
        answer = 0
        for num in nums :
            sums +=num
            if sums - k in prifixSum :
                answer += prifixSum[sums-k]
            prifixSum[sums]=1+prifixSum.get(sums,0)
        return answer 
        
       