class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a list of tuples containing the scores and their indices
        score_indices = [(s, i) for i, s in enumerate(score)]
        # Sort the list of tuples based on scores in reverse order
        score_indices.sort(reverse=True)
        
        # Assign ranks based on the sorted indices
        ranks = [""] * len(score)
        for i, (s, index) in enumerate(score_indices):
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)
        
        return ranks