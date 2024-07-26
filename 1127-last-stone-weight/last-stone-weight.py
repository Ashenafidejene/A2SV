class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negativStones = [-i for i in stones]
        heapq.heapify(negativStones)
        while len(negativStones) >1:
            firstLarger = heapq.heappop(negativStones)
            secondLarger =heapq.heappop(negativStones)
            if firstLarger != secondLarger:
               heapq.heappush(negativStones,firstLarger-secondLarger)
        if len(negativStones) == 1:
            return -1*negativStones[0]
        return 0 