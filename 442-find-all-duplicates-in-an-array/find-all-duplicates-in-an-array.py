class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)  
        ans = []
        for num, count in counter.items():
            if count >= 2: 
                ans.append(num)
        return ans
