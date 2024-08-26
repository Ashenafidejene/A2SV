class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day = [1,7,30]
        @lru_cache
        def dfs(i):
            if i >= len(days):
                return 0
            minimal = float("inf")
            for k in range(len(day)):
                j = i
                while j < len(days) and days[j] < days[i] + day[k]:
                    j += 1
                minimal = min(minimal, costs[k] + dfs(j))
            return minimal
        return  dfs(0)


