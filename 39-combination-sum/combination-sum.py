class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def backTracking(comp,start):
            if sum(comp) == target:
                if comp.sort() in res :
                    return 
                res.append(comp.copy())
                return 
            if sum(comp) > target:
                return 
            for i in range(start, len(candidates)):
                comp.append(candidates[i])
                backTracking(comp, i)
                comp.pop()

        backTracking([],0)
        return res

        