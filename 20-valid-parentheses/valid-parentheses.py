class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        balance = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in '({[':
                balance.append(ch)
            elif balance and brackets[ch] == balance[-1]:
                balance.pop()
            else:
                return False
                
        return len(balance) == 0