class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0, len(nums) - 1, nums)
    
    def merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
        left, right = 0, 0
        merged_array = []
        
        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                merged_array.append(left_half[left])
                left += 1
            else:
                merged_array.append(right_half[right])
                right += 1
        
        merged_array.extend(left_half[left:])
        merged_array.extend(right_half[right:])
        return merged_array

    def mergeSort(self, left: int, right: int, arr: List[int]) -> List[int]:
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)
        
        return self.merge(left_half, right_half)