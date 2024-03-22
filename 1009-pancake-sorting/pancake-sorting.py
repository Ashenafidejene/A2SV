class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        nums = []
        while l != 0:
            ind = arr.index(max(arr[0: l]))
            self.reversefunction(arr, ind)
            nums.append(ind+1)
            self.reversefunction(arr, l-1)
            nums.append(l)
            l = l - 1
        return nums

    def reversefunction(self, arr: List[int], num: int):
        i = 0 
        while i < num:
            arr[i], arr[num] = arr[num], arr[i]
            i = i + 1 
            num = num - 1