class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows <= 2:
            return ans[:numRows]
        def dp(i):
            if i == numRows:
                return
            temp=[1]
            for j in range(1,i):
                temp.append(ans[i-1][j-1]+ans[i-1][j])
            temp.append(1)
            ans.append(temp)
            dp(i+1)
        dp(2)
        return ans 

       