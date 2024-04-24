class Solution:
    def removeStars(self, s: str) -> str:
        answer = ""
        reverseS = s[::-1]  # Reverse the string using slicing
        count = 0 
        for char in reverseS:
            if char == '*':
                count += 1
            elif count != 0:
                count -= 1
            else:
                answer = char + answer 
        return answer 