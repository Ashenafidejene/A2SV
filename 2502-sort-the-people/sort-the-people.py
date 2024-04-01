class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for i in range(size):
            min_idx = i
            for j in range(i + 1, size):
                if heights[min_idx] < heights[j]:
                    min_idx = j
            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            names[i], names[min_idx] = names[min_idx], names[i]
                
        return names
