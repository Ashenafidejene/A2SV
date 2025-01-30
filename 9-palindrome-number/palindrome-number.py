class Solution:
    def isPalindrome(self, x: int) -> bool:
        strs = str(x)
        return strs == strs[::-1]