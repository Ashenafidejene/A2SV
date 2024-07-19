class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    right_count += 1
                    merged.append(right[j])
                    j += 1
                else:
                    merged.append((left[i][0], left[i][1] + right_count, left[i][2]))
                    i += 1
            while i < len(left):
                merged.append((left[i][0], left[i][1] + right_count, left[i][2]))
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged
        
        def mergeSort(arr, left, right):
            if left == right:
                return [(arr[left], 0, left)]  # Include original index
            mid = left + (right - left) // 2
            left_half = mergeSort(arr, left, mid)
            right_half = mergeSort(arr, mid + 1, right)
            return merge(left_half, right_half)

        # Start merge sort and get the answer
        answer = mergeSort(nums, 0, len(nums) - 1)
        # Initialize result array with the same length as nums
        result = [0] * len(nums)
        # Fill the result array using the counts from answer
        for value, count, original_index in answer:
            result[original_index] = count
        return result