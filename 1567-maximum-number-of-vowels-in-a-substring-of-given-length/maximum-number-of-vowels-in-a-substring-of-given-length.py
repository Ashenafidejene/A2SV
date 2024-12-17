class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = {}
        value = set("aeiou")
        lenV=0
        lenC=0
        
        for i in range(k):
            if s[i] in value :
                lenV +=1
            else:
                lenC+=1
        maxV=lenV
        for r in range(k,len(s)):
            if s[r] in value:
                lenV +=1
            else:
                lenC+=1
            if s[r-k] in value:
                lenV-=1
                lenC+=1
            maxV = max(maxV,lenV)
        return maxV
