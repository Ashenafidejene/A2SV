class Solution:
    def balancedString(self, s: str) -> int:
        LatterNumber = len(s) / 4
        counter = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            counter[char] += 1
        if min(counter.values()) == LatterNumber:
            return 0
        left = 0
        answer = len(s) + 1
        for right in range(len(s)):
            counter[s[right]] -= 1
            while all(counter[char] <= LatterNumber for char in 'QWER') and right >= left:
                answer = min(answer, right - left + 1)
                counter[s[left]] += 1
                left += 1
        return 0 if answer == len(s) + 1 else answer