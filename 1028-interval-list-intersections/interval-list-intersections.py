class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f, s = 0 , 0 
        answer = []
        if len(firstList) == 0 or len(secondList)==0 :
            return answer
        while f < len(firstList) and s < len(secondList):
            mins = max(firstList[f][0],secondList[s][0])
            maxd = min(firstList[f][1],secondList[s][1])
            if maxd>=mins :
                answer.append([mins,maxd])
            
            if maxd == secondList[s][1]:
                s+=1
            else:
                f+=1
        return answer 


        
        