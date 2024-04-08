class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return s1 == s2 
        countS1 = {}
        countS2 = {}
        for indx in range(len(s1)):
            countS1[s1[indx]] = 1 + countS1.get(s1[indx],0)
            countS2[s2[indx]] = 1 + countS2.get(s2[indx],0)
        if countS1 == countS2:
            return True 
        left = 0 
        for right in range(len(s1),len(s2)):
            countS2[s2[right]] =1+ countS2.get(s2[right],0)
            countS2[s2[left]] -= 1 
            if countS2[s2[left]] == 0 :
                countS2.pop(s2[left])
            left+=1
            if countS1 == countS2:
               return True 
        return False 
