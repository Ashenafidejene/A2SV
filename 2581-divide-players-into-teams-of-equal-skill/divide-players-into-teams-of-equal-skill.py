class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = skill[0]+skill[-1]
        sums = 0 
        l,r =  0 , len(skill)-1
        while l<r :
            if skill[l]+skill[r] != check:
                return -1
            sums += skill[l]*skill[r]
            l+=1
            r-=1
        return sums
    
