class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums = [0] * (len(s) + 1)  # Extra element to handle the end index without bounds check
        
        for shift in shifts:
            start, end, direction = shift
            if direction == 1:
                nums[start] += 1
                if end + 1 < len(nums):
                    nums[end + 1] -= 1
            else:
                nums[start] -= 1
                if end + 1 < len(nums):
                    nums[end + 1] += 1
        
        # Cumulative sum to get the net shifts at each position
        for i in range(1, len(s)):
            nums[i] += nums[i - 1]
        
        answer = ""
        for i in range(len(s)):
            # Calculate the new character after shifting
            char = ord(s[i]) - ord('a') + nums[i]
            char = (char % 26 + 26) % 26  # Ensure it wraps correctly within 0-25 range
            answer += chr(char + ord('a'))
        
        return answer
