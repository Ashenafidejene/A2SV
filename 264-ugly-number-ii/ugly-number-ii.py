class Solution:
    def nthUglyNumber(self, n: int) -> int:
        answer = [1]
        p2,p3,p5 = 0,0,0
        m2,m3,m5 = 2,3,5
        lE = 1 
        while len(answer) < n :
            lE = min(m2,m3,m5)
            if lE != answer[-1]:
                answer.append(lE)
            if lE == m2 :
                p2+=1
                m2 =answer[p2]*2
            elif lE == m3 :
                p3+=1
                m3 = answer[p3]*3
            else:
                p5+=1
                m5 = answer[p5]*5
    
        return answer[n-1]

        

