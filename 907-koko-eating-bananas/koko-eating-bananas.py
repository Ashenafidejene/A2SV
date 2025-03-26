class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = right
        while left <= right:
            k = (left + right)//2
            hours = 0 
            for p in piles :
                hours +=math.ceil(p/k)
            if hours <= h:
               res = min(res,k)
               right = k -1
            else:
                left = k+1
        return res