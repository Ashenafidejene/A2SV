class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        answer = []
        def permutation():
            if len(path) == len(nums):
                answer.append(path[:])
                return 
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                permutation()
                path.pop()
        permutation()
        return answer

        