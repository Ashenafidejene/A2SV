class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxs = 1
        left = 0 
        for index in range(len(arr)-1):

            if index % 2 == 0 :
                if arr[index] >=arr[index + 1]:
                    left = index+1
                    continue 
            else :
                if arr[index] <= arr[index + 1]:
                    left = index+1 
                    continue 
            maxs = max(maxs, index - left + 2)
        left = 0 
        for indx in range(len(arr)-1):
            
            if indx % 2 != 0 :
                if arr[indx] >= arr[indx + 1]:
                    left = indx + 1
                    continue 
            else :
                if arr[indx] <= arr[indx + 1]:
                    left = indx+1
                    continue
            maxs = max(maxs, indx - left + 2)
        return maxs