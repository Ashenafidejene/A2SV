class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)  # Convert the number to its binary representation
        stor = '0b'  # Initialize a new binary string for the complement
        for i in range(2, len(s)):  # Start from index 2 to skip '0b' prefix
            if s[i] == '0':
                stor += '1'
            else:
                stor += '0'
        return int(stor, 2)