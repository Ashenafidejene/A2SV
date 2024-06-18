class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        answer = self.Kthbit("0", 1, n)
        return answer[k-1]
    
    def reverse(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            if s[i] == '0':
                answer += '1'
            else:
                answer += '0'
        return answer[::-1]
    
    def Kthbit(self, s: str, index: int, target: int) -> str:
        if index == target:
            return s
        s = s + '1' + self.reverse(s)
        return self.Kthbit(s, index + 1, target)