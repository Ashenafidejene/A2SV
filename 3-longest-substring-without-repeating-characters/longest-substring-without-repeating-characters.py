class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0 
        substring = 0 
        for right in range(len(s)) :
            while s[right] in charset:
                charset.remove(s[left])
                left +=1 
            charset.add(s[right])
            substring = max ( substring, right-left+1 )
        return substring