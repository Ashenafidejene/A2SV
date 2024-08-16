class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def handler(level , ind ):
            triangle[i][j] +=min(triangle[i+1][j],triangle[i+1][j+1])


        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                handler(i,j)
        return triangle[0][0]
        