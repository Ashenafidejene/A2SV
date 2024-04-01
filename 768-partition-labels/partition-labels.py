class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count={}
        for i in range(len(s)):
            count[s[i]] = i 
        maxs = 0 
        lastIndex =0 
        answer=[]
        for value , indexs in count.items():
            if maxs >= s.index(value):
                maxs = max(maxs , indexs)
            else :
                
                answer.append(maxs-lastIndex)
                lastIndex=maxs
                maxs =  indexs 
        answer.append(maxs-lastIndex)
        answer[0]+=1
        return answer 
            