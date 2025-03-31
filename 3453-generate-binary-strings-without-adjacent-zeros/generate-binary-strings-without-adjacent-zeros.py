class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def builder(strs,flag):
            if len(strs) == n :
                ans.append(strs)
                return 
            if (flag):
                builder(strs+"0",False)
            builder(strs+"1",True)
        builder("",True)
        return ans

                

        