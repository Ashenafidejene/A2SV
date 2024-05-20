class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        num = [0] * ( n + 1)
        for i in range(len(bookings)):
            num[bookings[i][0]-1]+=bookings[i][2]
            num[bookings[i][1]]-=bookings[i][2]
        for j in range(1,len(num)):
            num[j] = num[j]+num[j-1]

        return num[0:n]