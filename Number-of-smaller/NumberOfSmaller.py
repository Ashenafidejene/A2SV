def count_smaller_elements(arr1, arr2):
    counts = []
    for num in arr2:
        left = 0
        right = len(arr1) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr1[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        counts.append(left)
    return counts

# Input processing
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Calling the function and printing the output
result = count_smaller_elements(arr1, arr2)
print(*result)