class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for char in s :
            counter[char] = 1+counter.get(char,0)
        longest_palindrome = 0
        has_odd_count = False
        
        for count in counter.values():
            if count % 2 == 0:
                longest_palindrome += count
            else:
                longest_palindrome += count - 1
                has_odd_count = True
        
        if has_odd_count:
            longest_palindrome += 1
        
        return longest_palindrome
        
        