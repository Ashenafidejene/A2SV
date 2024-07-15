class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s):
            char_set = set(s)
            for i, c in enumerate(s):
                if c.swapcase() not in char_set:
                    left = helper(s[:i])
                    right = helper(s[i+1:])
                    return max(left, right, key=len)
            return s
        
        return helper(s)