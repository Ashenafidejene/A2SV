class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = set(arr)
        sortedarr = list(rank)
        sortedarr.sort()
        count = {}
        for x in range(len(sortedarr)):
            count[sortedarr[x]] = x+1
        ans = []
        for val in arr:
            ans.append(count[val])
        return ans 