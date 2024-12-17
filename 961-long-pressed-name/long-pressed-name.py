class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        if len(name)==len(typed):
            return name == typed
        f , s = 0,0 
        while s < len(typed) and f < len(name):
            if name[f]==typed[s]:
                f+=1
                s+=1
            elif name[f]!=typed[s] and s >0 and typed[s] == typed[s-1]:
                s+=1
            else:
                return False
        if s == len(typed) and f <len(name):
            return False
        for k in range(s,len(typed)):
            if typed[k]!=name[-1]:
                return False
        return True 


