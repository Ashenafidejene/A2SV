class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(comp,index):
            if sum(comp) == target :
                ans.append(comp[:])
            if sum(comp) < target:
                for i in range(index , len(candidates)):
                    comp.append(candidates[i])
                    backtracking(comp,i)
                    comp.pop()
        backtracking([],0)
        return ans

