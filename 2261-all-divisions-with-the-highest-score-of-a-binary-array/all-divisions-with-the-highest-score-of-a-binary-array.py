class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        countZeros=0 
        for num in nums :
            if num == 0 :
                countZeros = countZeros + 1 
        countOne = 0 
        for i in range(len(nums)-1, -1, -1):
            temp=nums[i]
            nums[i] = countZeros + countOne
            if temp == 1:
                countOne = countOne + 1
            else :
                countZeros = countZeros - 1 
        max_num = max(nums)
        max_num =max ( max_num,countOne )
        answer = []
        if max_num== countOne  :
            answer.append(0)
        for k in range(len(nums)):
            if nums[k] == max_num:
                answer.append(k+1)
        return answer               