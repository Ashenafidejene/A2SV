class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len( typed):
            return False 
        if len(name) == len( typed):
            return name == typed 
        if len(name) == 1:
            for char in  typed:
                if char != name[0]:
                    return False 
            return True 
        n , t = 0,0 
        while n < len(name)-1 or t < len( typed)-1:
            if n < len(name)-1 and t < len( typed) -1 :
                if name[n:n+2] == typed[t:t+2]:
                    n+=1
                    t+=1
                elif typed[t] == typed[t+1]:
                    t+=1
                else :
                    return False
            elif t < len( typed) -1 and n >= len(name)-1:
                if typed[t] == typed[t+1]:
                    t+=1
                else :
                    return False
            else:
                return False
        return True



