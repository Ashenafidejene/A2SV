
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins , maxs = arrays[0][0] , arrays[0][-1]
        res = 0 
        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, arr[-1] - mins, maxs - arr[0])
            mins = min(mins, arr[0])
            maxs = max(maxs, arr[-1])
        return res