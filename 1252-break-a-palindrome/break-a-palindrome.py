class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1 :
            return "" 
        answer=""
        flag= True 
        for i in range(len(palindrome)):
            if palindrome[i]!='a' and flag :
               answer += 'a'
               flag=False
            else :
                answer += palindrome[i]
        
        for char in answer :
            if char != 'a':
               return answer
        final = palindrome[0:len(palindrome)-1]
        final +='b'
        return final
                
         

        