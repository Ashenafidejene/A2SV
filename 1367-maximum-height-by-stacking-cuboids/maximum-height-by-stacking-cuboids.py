

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort each cuboid's dimensions to ensure consistent orientation
        for cuboid in cuboids:
            cuboid.sort()
        
        # Sort cuboids based on dimensions
        cuboids.sort()
        
        n = len(cuboids)
        heights = [0] * n
        
        for i in range(n):
            heights[i] = cuboids[i][2]  # Initialize with the height of the current cuboid
            for j in range(i):
                if self.canBeStacked(cuboids[j], cuboids[i]):
                    heights[i] = max(heights[i], heights[j] + cuboids[i][2])
        
        return max(heights)

    def canBeStacked(self, bottom: List[int], top: List[int]) -> bool:
        return bottom[0] <= top[0] and bottom[1] <= top[1] and bottom[2] <= top[2]