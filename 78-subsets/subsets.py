class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i,path,length):
            if len(path) == length:
                ans.append(path[:])
                return 
            for j in range(i , len(nums)):
                path.append(nums[j])
                backtrack(j+1,path,length)
                path.pop()

        for l in range(len(nums)+1):
            backtrack(0,[],l)
        return ans

        