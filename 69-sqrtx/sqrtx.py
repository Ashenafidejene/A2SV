class Solution:
    def mySqrt(self, x: int) -> int:
        start , end = 1 , x 
        mid = (start + end)//2
        while start <= end :
            if mid*mid == x:
                return mid
            if mid*mid > x :
                end = mid -1 
            else :
                start = mid+1
            mid = (start + end)//2
        return mid 