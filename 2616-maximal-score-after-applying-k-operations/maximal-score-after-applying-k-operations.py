class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        negativ =[ -i for i in nums]
        heapq.heapify(negativ)
        totalSum=0
        while k >0:
            temp = heapq.heappop(negativ)
            totalSum = totalSum - temp 
            heapq.heappush(negativ,math.floor(temp/3))
            k-=1
        return totalSum 

