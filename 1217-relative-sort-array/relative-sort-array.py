class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        answer = []
        
        # Count occurrences of elements in arr1
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        # Append elements from arr2 according to their occurrences in arr1
        for val in arr2:
            if val in count:
                answer.extend([val] * count[val])
                del count[val]  # Remove the element from count
        
        # Append remaining elements in count sorted by their keys
        for val, freq in sorted(count.items()):
            answer.extend([val] * freq)
        
        return answer
