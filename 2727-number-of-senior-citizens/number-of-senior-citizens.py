class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0 
        for passager in details:
            if passager[11] > '6':
                counter+=1
            elif passager[11]=='6':
                if passager[12] != '0':
                    counter+=1
        return counter 