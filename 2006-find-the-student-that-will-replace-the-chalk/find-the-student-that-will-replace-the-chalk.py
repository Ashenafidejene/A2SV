class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 1:
            return 0
        sums = sum(chalk)
        while k >= sums:
            k-=sums
        
        i=0
        while chalk[i] <= k:
            k -=chalk[i]
            i+=1
            if i == len(chalk):
                i=0
        return i