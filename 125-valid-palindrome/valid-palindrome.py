class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l , r = 0, len(k)-1
        while l < r:
            if k[l] != k[r]:
                return False 
            l+=1
            r-=1
        return True 



        
        