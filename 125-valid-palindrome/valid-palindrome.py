class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = ""
        for char in s:
             if char.isalnum():
                answer = answer + char.lower()
        reverse = answer[::-1]
        return reverse == answer 



        
        