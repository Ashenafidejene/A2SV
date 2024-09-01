class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) % n != 0:
            return []
        ans=[]
        i , l = 0,n
        while l <=len(original):
            ans.append(original[i:l])
            i=l
            l+=n
        if len(ans) != m:
            return []
        return ans 