class Solution:
    def minSwaps(self, s: str) -> int:
        close , maxclose =0,0
        for cr in s:
            if cr =='[':
                close -=1
            else:
                close += 1
            maxclose=max(maxclose,close)
        return (maxclose+1)//2