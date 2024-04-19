class NumArray:

    def __init__(self, nums: List[int]):
       self.PrifixSum = [0] 
       for num in nums :
           self.PrifixSum.append(self.PrifixSum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.PrifixSum[right+1] - self.PrifixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)