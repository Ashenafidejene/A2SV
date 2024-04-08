class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxV = 0 
        count = {"vowels": 0, "consonant": 0}
        for i in range(k):
            count[self.VauleOrnot(s[i])] += 1 
        maxV = count["vowels"]
        left = 0 
        for ind in range(k, len(s)):
            count[self.VauleOrnot(s[ind])] += 1 
            count[self.VauleOrnot(s[left])] -= 1
            maxV = max(maxV, count["vowels"])
            if maxV == k:
                return k 
            left+=1
        return maxV

    def VauleOrnot(self, s: str) -> str:
        if s == 'a' or s == 'u' or s == 'o' or s == 'i' or s == 'e':
            return "vowels"
        return "consonant"