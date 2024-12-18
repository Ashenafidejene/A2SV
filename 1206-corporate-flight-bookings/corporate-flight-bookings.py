class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prifixSum = [0]*(n+1)
        for order in bookings :
            first,last,seat = order
            prifixSum[first-1]+=seat
            prifixSum[last]-=seat
        acumulator = 0
        for i in range(1,len(prifixSum)):
            prifixSum[i]+=prifixSum[i-1]
        return prifixSum[0:n]
        