class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
       
        memo = {}

        def get_value(row, col):
           
            if col == 0 or col == row:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
           
            memo[(row, col)] = get_value(row - 1, col - 1) + get_value(row - 1, col)
            return memo[(row, col)]

       
        return [get_value(rowIndex, col) for col in range(rowIndex + 1)]