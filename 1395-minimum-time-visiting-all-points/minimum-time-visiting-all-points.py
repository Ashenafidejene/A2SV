class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        countPath =  0 
        MaxDistance = 0
        for i in range(len(points)-1):
            MaxDistance = max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
            countPath = countPath + MaxDistance
        return countPath