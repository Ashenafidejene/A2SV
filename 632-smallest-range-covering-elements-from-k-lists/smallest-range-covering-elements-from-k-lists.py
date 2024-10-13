class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to store the (value, list_index, element_index)
        min_heap = []
        max_val = float('-inf')  # To track the maximum value in the current range
        k = len(nums)
        
        # Initialize the heap with the first element from each list
        for i in range(k):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])  # Update the maximum value
        
        # Track the best range found
        best_range = [float('-inf'), float('inf')]
        
        while min_heap:
            min_val, list_index, element_index = heapq.heappop(min_heap)
            
            # Update the best range if the current range is smaller
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]
            
            # If the current list is exhausted, break the loop
            if element_index + 1 == len(nums[list_index]):
                break
            
            # Get the next element from the same list
            next_val = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
            
            # Update the max value in the current window
            max_val = max(max_val, next_val)
        
        return best_range