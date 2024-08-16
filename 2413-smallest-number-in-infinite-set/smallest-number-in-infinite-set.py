class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1, 1001)]
        heapq.heapify(self.nums)
        self.nums_set = set(self.nums)

    def popSmallest(self) -> int:
        if len(self.nums):
            smallest = heapq.heappop(self.nums)
            self.nums_set.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num not in self.nums_set:
            heapq.heappush(self.nums, num)
            self.nums_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)