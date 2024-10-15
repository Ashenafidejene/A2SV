class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = [0]+flowerbed+[0]
        count = 0
        for j in range(1,len(ans)-1):
            if ans[j]!=1 and ans[j-1] !=1 and ans[j+1] !=1:
               count +=1
               ans[j]=1

        return count >= n