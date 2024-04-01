
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):  # Assuming 32-bit integers
            result <<= 1  # Left shift result to make space for the next bit
            result |= n & 1  # Extract the least significant bit of n and set it in result
            n >>= 1  # Right shift n to process the next bit
        return result