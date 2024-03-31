class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        k=[9,8,7,6,5,4,3,2,1,0]

        if len(arr) < 3 or k == arr:
            return False 
        flag = True  
        first = True 
            
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] and flag :
                flag=False
            elif arr[i] < arr[i+1] and not flag:
                return False 
            elif arr[i]==arr[i+1]:
                return False
        
        return not flag  
