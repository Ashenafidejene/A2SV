class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for index , value in count.items():
            if value >=2:
                return index
        return 0 