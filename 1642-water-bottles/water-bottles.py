class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        Total = 0
        while numBottles >= numExchange:
            Total += numExchange
            numBottles -= numExchange - 1
        Total += numBottles
        return Total 