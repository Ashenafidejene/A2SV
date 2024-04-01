class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity 
        steps  = 0 
        for i in range(len(plants)) :
            if plants[i] <= cap:
               steps = steps + 1
               cap = cap - plants[i]
            else :
                steps = steps  +  (2*i) + 1 
                cap = capacity  -plants[i]
        return steps 