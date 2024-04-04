class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxs= 0
        for i in range(len(points)-1):
            maxs=max(maxs,(points[i+1][0]-points[i][0]))
        return maxs 