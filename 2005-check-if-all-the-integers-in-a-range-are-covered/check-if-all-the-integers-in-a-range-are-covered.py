class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges,key=lambda x: x[0])
        for l,r in ranges:
            while l <= left <= r:
                left += 1
        return left > right