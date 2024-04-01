class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum= 0 
        skill.sort()
        check= skill[0] + skill[len(skill)-1]
        r , l = len(skill)-1,0
        answer = 0 
        while r > l :
            if skill[r] + skill[l] != check:
                return -1 
            answer += skill[r]*skill[l]
            r -= 1 
            l+=1
        return answer 


 