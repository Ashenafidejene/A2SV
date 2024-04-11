class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [str(x) for x in nums]

        # Custom comparison function to sort numbers as strings
        def compare(x, y):
            return int(y + x) - int(x + y)

        sorted_nums = sorted(num_str, key=cmp_to_key(compare))
        # Join the sorted numbers to form the largest possible number
        return str(int(''.join(sorted_nums)))