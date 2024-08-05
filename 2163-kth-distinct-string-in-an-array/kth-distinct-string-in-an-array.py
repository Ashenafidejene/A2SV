class Solution:
       def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = {}
        ans = []
        
       
        for i in arr:
            counter[i] = 1 + counter.get(i, 0)
        
        
        for value, count in counter.items():
            if count == 1:
                ans.append(value)
        
       
        return ans[k-1] if len(ans) >= k else ""