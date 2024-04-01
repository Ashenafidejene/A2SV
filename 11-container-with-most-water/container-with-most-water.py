class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxs=0
        width = len(height)-1
        r , l = len(height)-1,0
        while l < r :
            maxs = max (maxs , (width * min(height[r],height[l])))
            if height[r] > height[l] :
                l += 1 
            else :
                r -= 1 
            width -= 1 
        return maxs 

