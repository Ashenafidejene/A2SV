class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        k = len(piles)/3
        sum= 0 
        for i in range(len(piles)):
            if i % 2 == 1:
                sum = piles[i] + sum
                k = k -1 
            if k == 0 :
                break 
        return sum 
             
            

            