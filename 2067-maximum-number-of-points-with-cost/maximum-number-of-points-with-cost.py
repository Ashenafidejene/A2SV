class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        
        # Iterate from the second-to-last row to the top row
        for i in range(rows - 2, -1, -1):
            # Create a temporary array to store the max values
            left = [0] * cols
            right = [0] * cols
            
            # Calculate max points when moving left to right
            left[0] = points[i + 1][0]
            for j in range(1, cols):
                left[j] = max(left[j - 1] - 1, points[i + 1][j])
            
            # Calculate max points when moving right to left
            right[-1] = points[i + 1][-1]
            for j in range(cols - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, points[i + 1][j])
            
            # Update the current row with the maximum of the left and right values
            for j in range(cols):
                points[i][j] += max(left[j], right[j])
        
        return max(points[0])