class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        count = 0
        left = 0
        if total >= threshold * k:
            count += 1
        for right in range(k, len(arr)):
            total -= arr[left]
            total += arr[right]
            left += 1
            if total >= threshold * k:
                count += 1
        return count