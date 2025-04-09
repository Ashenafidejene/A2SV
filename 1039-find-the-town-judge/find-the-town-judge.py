class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_adragi  = set()
        trust_tederagi = {i:1 for i in  range(1,n+1)}
        for truster , judge in trust :
            trust_adragi.add(truster)
            trust_tederagi[judge] +=1
        for i in range(1,n+1):
            if not (i in trust_adragi):
                if trust_tederagi[i] == n :
                    return i 
        return -1
