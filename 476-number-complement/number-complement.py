class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)  
        stor = '0b'  
        for i in range(2, len(s)):  
            if s[i] == '0':
                stor += '1'
            else:
                stor += '0'
        return int(stor, 2)