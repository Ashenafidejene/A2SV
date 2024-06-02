class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        array = [cost[0],cost[1]]
        for index in range ( 2 , len(cost)):
            array.append(min(array[index-1],array[index-2])+cost[index])
        return  min(array[-1], array[-2])
