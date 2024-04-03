class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) : return []
        Pcounter , scounter = {},{}
        for i in range(len(p)):
            Pcounter[p[i]] = 1 + Pcounter.get(p[i],0)
            scounter[s[i]] = 1 + scounter.get(s[i],0)
        res = [0] if Pcounter == scounter else []
        left = 0 
        for right in range(len(p),len(s)):
            scounter[s[right]] = 1 + scounter.get(s[right],0)
            scounter[s[left]] -= 1
            if scounter[s[left]] == 0 :
               scounter.pop(s[left])
            left+=1
            if Pcounter == scounter :
                res.append(left)
        return res 