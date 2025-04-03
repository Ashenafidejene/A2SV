class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        def backtracking(i, j, currentIndex):
            # Base case: if index reaches the end of the word, return True
            if currentIndex == len(word):
                return True 

            # Check boundaries and character match
            if (i, j) in visit or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[currentIndex]:
                return False  

            # Mark the cell as visited
            visit.add((i, j))

            # Explore all four possible directions
            found = (
                backtracking(i - 1, j, currentIndex + 1) or  # Up
                backtracking(i + 1, j, currentIndex + 1) or  # Down
                backtracking(i, j - 1, currentIndex + 1) or  # Left
                backtracking(i, j + 1, currentIndex + 1)     # Right
            )

            # Backtrack: unmark the cell
            visit.remove((i, j))

            return found
        for i in range(len(board)):
            for  j in range(len(board[i])):
                if backtracking(i,j,0):
                    return True 
        return False

