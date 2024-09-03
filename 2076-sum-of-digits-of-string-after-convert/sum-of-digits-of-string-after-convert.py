class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def changer(latter):
            ans = ""
            for char in latter:
                ans += str(ord(char) - ord('a') + 1)
            return ans
        
        def helper(latter, k):
            if k == 0:
                return int(latter)
            temp = sum(int(char) for char in latter)
           
            return helper(str(temp), k - 1)

        r = changer(s)
        return helper(r, k)