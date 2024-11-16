class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location = max(trip[2] for trip in trips)
        prifixSum = [0]*(max_location+1)
        for tripP in trips:
            prifixSum[tripP[1]]+=tripP[0]
            prifixSum[tripP[2]]-=tripP[0]
        current_passagenr = 0
        for i in range(len(prifixSum)) :
                current_passagenr=current_passagenr+prifixSum[i]
                if current_passagenr > capacity:
                    return False
        return True 
