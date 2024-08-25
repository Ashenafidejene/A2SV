class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        @lru_cache(None)
        def dp(index):
            if index >= len(pairs):
                return 0
            option1 = dp(index + 1)
            next_index = index + 1
            while next_index < len(pairs) and pairs[next_index][0] <= pairs[index][1]:
                next_index += 1
            option2 = 1 + dp(next_index)
            return max(option1, option2)
        
        return dp(0)
