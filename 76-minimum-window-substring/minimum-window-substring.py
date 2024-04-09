class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        answer = ""
        maxLen = len(s) + 1
        counterT = {}
        counterS = {}
        
        for char in t:
            counterT[char] = 1 + counterT.get(char, 0)
            counterS[char] = 0
        
        left = 0
        for right in range(len(s)):
            if s[right] in counterT:
                counterS[s[right]] += 1
            while self.equalityChecker(counterS, counterT):
                if maxLen > (right - left + 1):
                    maxLen = right - left + 1
                    answer = s[left:right + 1]
                if s[left] in counterT:
                    counterS[s[left]] -= 1
                left += 1
        
        return answer

    def equalityChecker(self, counterS: dict, counterT: dict) -> bool:
        for char in counterT:
            if counterS.get(char, 0) < counterT[char]:
                return False
        return True