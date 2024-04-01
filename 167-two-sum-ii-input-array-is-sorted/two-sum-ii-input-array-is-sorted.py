class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last , first = len(numbers)-1 , 0 
        while last != first :
            if numbers[last] + numbers[first] == target :
                return [first+1,last+1]
            elif numbers[last] + numbers[first] > target :
                last -=1
            else:
                first +=1 
        return [-1,-1]