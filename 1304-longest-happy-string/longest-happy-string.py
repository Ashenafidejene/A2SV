class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heapMax , res = [],""
        
       
        for val, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if val != 0:
                heapq.heappush(heapMax, (val, char))
        
        while heapMax:
            val, char = heapq.heappop(heapMax)
            
            # Check if the last two characters are the same as the current one
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heapMax:
                    break 
                
                
                val1, char2 = heapq.heappop(heapMax)
                res += char2
                val1 += 1  
                
                
                if val1:
                    heapq.heappush(heapMax, (val1, char2))
                
               
                heapq.heappush(heapMax, (val, char))
            else:
                
                res += char
                val += 1  
                
            
                if val:
                    heapq.heappush(heapMax, (val, char))
        
        return res
                