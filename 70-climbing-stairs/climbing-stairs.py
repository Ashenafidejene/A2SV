class Solution:
    def climbStairs(self, n: int) -> int:
        array = [1,1]
        for index in range(2,n+1):
            array.append(array[index-1] + array[index-2])
        return array[n]

        