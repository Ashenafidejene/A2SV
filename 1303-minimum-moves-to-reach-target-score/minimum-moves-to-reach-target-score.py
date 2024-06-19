class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0 
        while target >1:
            if target%2==0 and maxDoubles >0:
                target//=2
                count+=1
                maxDoubles-=1
            else:
                if maxDoubles == 0 :
                   target -= 1
                   count += target
                   return count 
                     
                target-=1
                count+=1
        return count 