class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        negative_values = [-p for p in piles]
        
        total_sum = sum(piles)
        heapq.heapify(negative_values)
        while k > 0:
            largest = heapq.heappop(negative_values)
            reduce_value = math.floor(-largest / 2)
            total_sum -=  reduce_value
            heapq.heappush(negative_values,largest + reduce_value)
            k -= 1
        return total_sum
