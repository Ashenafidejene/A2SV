class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people) - 1 
        if len(people) == 1 :
            return 1 
        count = 0 
        while l <= r:
            if  people[l] + people[r] <= limit :
                r -=1 
                l +=1 
                count +=1
            else:
                r-=1 
                count +=1
        return count 
