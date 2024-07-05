class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        self.minUnafairness = float('inf')
        def backtrack(i , bucket):
            if i >= len(cookies):
               self.minUnafairness = min(self.minUnafairness,max(bucket))
               return 
            for j in range(k):
                if bucket[j] + cookies[i] >= self.minUnafairness:
                    continue
                bucket[j] += cookies[i]
                backtrack(i+1,bucket)
                bucket[j] -= cookies[i]
        backtrack(0,bucket)
        return self.minUnafairness
        