class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0 
        sum = 0 
        maxLength = 0 
        for i in range(len(s)):
            if abs(ord(s[i]) - ord(t[i])) > maxCost:
                sum = 0 
                left = i + 1 
                continue 
            sum += abs(ord(s[i]) - ord(t[i]))
            while sum > maxCost:
                sum -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxLength = max(maxLength, i - left + 1)
        return maxLength
            