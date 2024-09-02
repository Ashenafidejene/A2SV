class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 1:
            return 0
        k = k % sum(chalk)
        
        i=0
        while chalk[i] <= k:
            k -=chalk[i]
            i+=1
            if i == len(chalk):
                i=0
        return i