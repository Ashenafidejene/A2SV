class Solution:
    def minLength(self, s: str) -> int:
        def recursion(k):
            i = 0
            while i < len(k) - 1:
               
                if k[i:i+2] == "AB" or k[i:i+2] == "CD":
                    
                    return recursion(k[:i] + k[i+2:])
                i += 1
            return k 
        
      
        final_string = recursion(s)
        return len(final_string)


