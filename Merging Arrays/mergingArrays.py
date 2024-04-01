def mergeArrays(arr1, arr2):
    mergedArray = []
    l, r = 0, 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            mergedArray.append(arr1[l])
            l += 1
        else:
            mergedArray.append(arr2[r])
            r += 1

    # If there are remaining elements in arr1 or arr2
    mergedArray.extend(arr1[l:])
    mergedArray.extend(arr2[r:])
    
    return mergedArray

# Input processing
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Merge arrays and print the result
mergedArray = mergeArrays(arr1, arr2)
print(*mergedArray)