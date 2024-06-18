class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = [0,0,0]
        if numOnes >k : 
            answer[0] =k 
            k = 0 
        if k >= numOnes :
            k -= numOnes
            answer[0] =numOnes

        if k < numZeros :
            answer[1] =k 
            k = 0 
        if k >=  numZeros :
            k -= numZeros
            answer[1] =numZeros  
        answer[2]=k
        return answer[0]*1 + answer[1]*0 + answer[2]*-1


        

