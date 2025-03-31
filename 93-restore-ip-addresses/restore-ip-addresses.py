class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtracking( strs, i, counter):
            if counter == 4 and i == len(s):
                ans.append(strs)
                return
            if counter >= 4 or i >= len(s):
                return

            if s[i] == "0":  
                if counter != 3:
                    backtracking( strs + "0.", i + 1, counter + 1)
                else:
                    backtracking( strs + "0", i + 1, counter + 1)
                return 

            for index in range(i + 1, len(s) + 1):
                if int(s[i:index]) <= 255:
                    temp = strs + s[i:index] + ('.' if counter < 3 else '')
                    backtracking( temp, index, counter + 1)
                else:
                    break
        backtracking("",0,0)
            
        return ans
                      
                   
                    