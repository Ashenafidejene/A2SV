class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def backTracking(comp,start):
            if sum(comp) == target:
                res.append(comp.copy())
                return 
            if sum(comp) > target:
                return 
            for i in range(start, len(candidates)):
                if i > start and candidates[i] ==candidates[i - 1]:
                    continue
                comp.append(candidates[i])
                backTracking(comp, i+1)
                comp.pop()
        backTracking([],0)
        return res
        