
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Define a custom sorting function based on the square root of the difference 
        # between the squares of the x and y coordinates
        def custom_sort(point):
            x, y = point
            return (x**2 + y**2) ** 0.5
        
        # Sort the points array based on the custom sorting function
        sorted_points = sorted(points, key=custom_sort)
        
        # Return the first k closest points
        return sorted_points[:k]