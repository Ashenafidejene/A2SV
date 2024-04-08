class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {"T":0,"F":0}
        left = 0 
        res = 0
    
        for right in range(len(answerKey)) : 
            count[answerKey[right]] += 1 
            while (right-left+1)- max(count.values()) > k:
                count[answerKey[left]] -=1
                left +=1 
            res = max(res, right-left + 1)
        return res 