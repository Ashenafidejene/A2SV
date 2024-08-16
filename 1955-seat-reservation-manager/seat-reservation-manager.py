class SeatManager:

    def __init__(self, n: int):
        self.Seat = [i for i in range(1,n+1)]
        heapq.heapify(self.Seat)

    def reserve(self) -> int:
        if len(self.Seat):
            return  heapq.heappop(self.Seat)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.Seat  , seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)