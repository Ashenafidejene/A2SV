class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        visit = set()
        original_color = image[sr][sc]
        
        def dfs(i, j):
            # Check if we are out of bounds or if the current pixel is not of the original color
            if i >= len(image) or j >= len(image[0]) or i < 0 or j < 0 or image[i][j] != original_color:
                return
            if (i, j) in visit:
                return 
            
            # Fill the current pixel with the new color
            image[i][j] = color
            visit.add((i, j))
            
            # Recursively call dfs on all 4 directions
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        
        dfs(sr, sc)
        return image
