class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def db(i , j):
            if i == len(s):
                return True 
            if j == len(t):
                return False 
            if s[i] == t[j]:
                return db(i+1,j+1)
            else :
                return db(i , j+1)
        return db(0,0)
