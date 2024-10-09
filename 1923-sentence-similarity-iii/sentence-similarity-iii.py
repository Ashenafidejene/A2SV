class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split sentences into words
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        # Ensure s1 is the shorter or equal length sentence
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        # Left pointer for comparing from the start
        l = 0
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
        
        # Right pointer for comparing from the end
        r = len(s1) - 1
        while r >= l and s1[r] == s2[len(s2) - len(s1) + r]:
            r -= 1
        
        # If all words in s1 match in s2, return True
        return l > r        # Split sentences into words
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        # Ensure s1 is the shorter or equal length sentence
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        # Left pointer for comparing from the start
        l = 0
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
        
        # Right pointer for comparing from the end
        r = len(s1) - 1
        while r >= l and s1[r] == s2[len(s2) - len(s1) + r]:
            r -= 1
        
        # If all words in s1 match in s2, return True
        return l > r