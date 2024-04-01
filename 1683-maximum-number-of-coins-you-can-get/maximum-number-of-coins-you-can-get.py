class Solution:
      def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        k = len(piles) // 3
        total = 0
        for i in range(1, len(piles), 2):
            total += piles[i]
            k -= 1
            if k == 0:
                break 
        return total
             
            

            