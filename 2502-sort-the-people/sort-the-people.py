class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Perform bubble sort
        for i in range(len(heights) - 1, 0, -1):
            # Last i elements are already in place
            for j in range(i):
                # Swap if the current element is smaller than the next element
                if heights[j] < heights[j + 1]:
                    names[j], names[j+1] = names[j+1], names[j] 
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        return names

