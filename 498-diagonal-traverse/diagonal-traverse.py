class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n - 1)]
        
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
        
        result = []
        for k, diagonal in enumerate(diagonals):
            if k % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)
        
        return result