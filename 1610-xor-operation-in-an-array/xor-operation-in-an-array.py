class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lastElement = start + (2*(n))
        nums = [i for i in range(start , lastElement,2)]
        result_reduce = reduce(lambda x, y: x ^ y, nums)
        return result_reduce
