class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        max_score = total 
        left = k - 1
        
        # Iterate from the right end of cardPoints
        for right in range(len(cardPoints) - 1, len(cardPoints) - k - 1, -1):
            total -= cardPoints[left]
            total += cardPoints[right]
            max_score = max(max_score, total)
            left -= 1 
        
        return max_score