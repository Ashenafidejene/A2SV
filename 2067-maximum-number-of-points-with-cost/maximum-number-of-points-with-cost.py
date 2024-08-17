class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        
        
        for i in range(rows - 2, -1, -1):
            
            left = [0] * cols
            right = [0] * cols
            

            left[0] = points[i + 1][0]
            for j in range(1, cols):
                left[j] = max(left[j - 1] - 1, points[i + 1][j])
            
     
            right[-1] = points[i + 1][-1]
            for j in range(cols - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, points[i + 1][j])
            
            
            for j in range(cols):
                points[i][j] += max(left[j], right[j])
        
        return max(points[0])